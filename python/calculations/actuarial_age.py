import datetime as dt
from datetime import date

def real_age(reference, born):

    try:
        ref_date = dt.datetime.strptime(reference, '%d/%m/%Y')
        bdate = dt.datetime.strptime(born, '%d/%m/%Y')

        try:
            birthday = bdate.date().replace(year = ref_date.date().year)
    
        # raised when birth date is February 29
        # and the current year is not a leap year
        except ValueError:
            birthday = bdate.date().replace(year = ref_date.date().year,
                    month = bdate.month + 1, day = 1)
    
        if birthday > ref_date.date():
            return ref_date.date().year - bdate.year - 1
        else:
            return ref_date.date().year - bdate.year
    
    except ValueError:
        print("Wrong date formats for Real Age")
        print("Reference:", reference)
        print("Birthday:", born)
  


def actuarial_age(born, start):
    
    try:
        bdate = dt.datetime.strptime(born, '%d/%m/%Y') #Birthday
        edate = dt.datetime.strptime(start, '%d/%m/%Y') #Effective date

        num_months = (edate.year - bdate.year) * 12 + (edate.month - bdate.month)
        
        if edate.day < bdate.day:
            num_days = 1
        else:
            num_days=0

        age = round((num_months-num_days)/12)

        return age

    except ValueError:
        print("Wrong date formats for Actuarial Age")
        print("Effective Date:", start)
        print("Birthday:", born)


def main():


    print("Please inform the date that you want to be the reference in the format: DD/MM/YYYY")
    reference_date = input()

    print("Please inform the birth date in the format: DD/MM/YYYY")
    birth_date = input()
    
    print("Please inform the Effective Date of the fd in the format: DD/MM/YYYY")
    effective_date = input()

    age_real = real_age(reference_date, birth_date)
    age_actuarial = actuarial_age(birth_date, effective_date)

    print("-----------Actuarial Age-------------")
    print("Real Age: ", age_real)
    print("Actuarial Age: ", age_actuarial)



if __name__ == "__main__":
    main()