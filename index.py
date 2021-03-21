import json
from abs_strategy import Screening
from patient.null_class import NullClass
from inspect import getmembers, isclass, isabstract
from patient.mis import Mis
from patient.s3 import S3
from uuid import uuid4
import patient


def handler(event, context):
    try:
        humans = {}
        class_list = getmembers(patient,
                                lambda m: isclass(m) and not isabstract(m))

        for name, _type in class_list:
            if isclass(_type) and issubclass(_type, patient.AbsPatient):
                humans.update([[name, _type]])

        sex = str(event['sex']).lower().capitalize()
        age = event['age']
        total_cholesterol = event['total_cholesterol']
        smoker = event['smoker']
        hdl_cholesterol = event['hdl_cholesterol']
        systolic_blood_pressure = event['systolic_blood_pressure']

        if sex in humans:
            result = dict()
            mis = Mis()
            s3 = S3()
            file = "sex: {} \n" \
                   "age: {}\n" \
                   "total_cholesterol: {}\n" \
                   "smoker: {}\n" \
                   "hdl_cholesterol: {}\n" \
                   "systolic_blood_pressure: {}".format(sex, age, total_cholesterol, smoker, hdl_cholesterol,
                                                        systolic_blood_pressure)
            file_id = "{}.txt".format(str(uuid4()))
            s3.upload_file_to_s3(file, "framscore", file_id, "framingham test data")
            human = humans[sex](age, total_cholesterol, smoker, hdl_cholesterol, systolic_blood_pressure)
            screening = Screening(human)
            result["your_results"] = screening.calculate_framingham()
            result["Males tested"] = mis.get_test_stats("male")
            result["Females tested"] = mis.get_test_stats("female")
        else:
            null_class = NullClass(sex)
            result = null_class.calculate_framingham()
        return {'statusCode': 400,
                'body': json.dumps(result),
                'headers': {'Content-Type': 'application/json'}
                }
    except KeyError as ex:
        return {'statusCode': 400,
                'body': json.dumps("The following error occurred: {}. Please provide the following input variables"
                                   "sex (S), age (N), total_cholesterol (N), smoker (true/false),"
                                   "hdl_cholesterol (N), systolic_blood_pressure(N)".format(ex)),
                'headers': {'Content-Type': 'application/json'}
                }
