import psycopg2
import requests
from XtenEngine.common_util import ResponseMessage
from XtenEngine.settings import CONNECTION, SECRET_KEY


class MeterService:
    def __init__(self, **kwargs):
        self.requests = requests
        self.token = kwargs.get('token', '')

    def getDataMeter(self):
        response_return = ResponseMessage()
        try:
            conn = psycopg2.connect(CONNECTION)
            cursor = conn.cursor()
            cursor.execute("select * from information_schema.tables where table_name=%s", ('meter',))
            query = """SELECT * FROM meter;"""
            if bool(cursor.rowcount):
                query = """SELECT * FROM public.meter tt 
                            INNER JOIN (SELECT sensor_id, MAX(time) AS MaxDateTime 
                            FROM public.meter GROUP BY sensor_id) groupedtt ON tt.sensor_id = groupedtt.sensor_id 
                            AND tt.time = groupedtt.MaxDateTime"""

            cursor.execute(query)
            records = cursor.fetchall()
            selectObject = []
            columnNames = [column[0] for column in cursor.description]

            setColumnResponse = []
            for key in columnNames:
                keyTemp = {
                    'columnDef': key,
                    'header': key.title().replace("_", " "),
                }
                setColumnResponse.append(keyTemp)

            for record in records:
                selectObject.append(dict(zip(columnNames, record)))

            response = {
                'column': setColumnResponse,
                'value': selectObject
            }

            response_return.set_success_status(response)

        except Exception as e:
            response_return.set_error_status(F'Exception Occurred {e}')

        return response_return.get_response()
