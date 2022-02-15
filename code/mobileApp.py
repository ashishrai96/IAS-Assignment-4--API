import requests

session = requests.Session()
HOST_URL = "http://localhost:8090"
ENDPOINTS = {
    "HELLO": "/hello",
    "GET_INFO": "/getInfo",
    "GET_INFO_LIST": "/getInfoList",
}

def get_data_from_cli():
    data = {
        "passengerId": int(input("Enter Passenger ID: ")),
        "pClass": int(input("Enter Passenger Class: ")),
        "name": input("Enter Passenger Name: "),
        "sex": input("Enter Passenger Gender (male/female): "),
        "age": float(input("Enter Passenger Age: ")),
        "sidSp": int(input("Enter Passenger Siblings: ")),
        "parch": int(input("Enter Passenger Parents: ")),
        "ticket": input("Enter Passenger Ticket No.: "),
        "fare": float(input("Enter Ticket Fare: ")),
        "cabin": input("Enter Passenger Cabin: "),
        "embarked": input("Enter Embarked (S/C/Q): ")
    }

    if(data["sex"]=="male"):
        data["sex"] = 0
    else:
        data["sex"] = 1

    if(data["embarked"] == "S"):
        data["embarked"] = 0
    elif(data["embarked"] == "C"):
        data["embarked"] = 1
    else:
        data["embarked"] = 2    

    return data


def getInfo():
    api = HOST_URL + ENDPOINTS["GET_INFO"]
    data = get_data_from_cli()
    arr = list()
    for k in data:
        if k not in ("passengerId", "name", "ticket", "cabin"):
            arr.append(data[k])

    has_surv = session.post(api, json={"data": arr}).content.decode('utf-8')
    print(has_surv)
    # resp = "The passenger has been "
    # if (int(has_surv) == 0):
    #     resp += "deceased."
    # else:
    #     resp += "survived."

    # print(resp)


def main():
    while True:
        getInfo()
        if(input("press q/Q to quit: ").lower() == "q"):
            break


if __name__=="__main__":
    main()
