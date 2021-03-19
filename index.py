import json
from abs_strategy import Screening
from patient.null_class import NullClass
from inspect import getmembers, isclass, isabstract
import patient


def handler(event, context):
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
        human = humans[sex](age, total_cholesterol, smoker, hdl_cholesterol, systolic_blood_pressure)
        screening = Screening(human)
        result = screening.calculate_framingham()
    else:
        null_class = NullClass(sex)
        result = null_class.calculate_framingham()
    return {'statusCode': 200,
            'body': json.dumps(result),
            'headers': {'Content-Type': 'application/json'}
            }
