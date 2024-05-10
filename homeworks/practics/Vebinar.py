def exp_exception():
    var = 1
    varstr = 'afg123'
    try:
        f = open("repka.txt")
        ABC
        if var > 3:
            raise Exception("Too less. Less then 3")
        elif varstr.isalpha():
            raise TypeError
        elif varstr.islower():
            raise BaseException
        print("Code works well")
    except TypeError:
        print("Wrong Type")
    except FileNotFoundError:
        print("File not found")
    except (NameError, ValueError):
        print("Something wrong")
    except BaseException:
        namelist = [1, 2, 3]
        print("Not Based")
        raise ValueError("Not good with Value...")
    else:
        print("Welldone")
    finally:
        print("It's finally")
        f.close()

exp_exception()
var = 1
varstr = 'afg'
try:
    f = open("repka.txt")
    if var > 3:
        raise Exception("Too less. Less then 31")
    elif varstr.isalpha():
        raise TypeError
    # elif varstr.islower():
    #     raise BaseException
    print("Code works well1")
except TypeError:
    print("Wrong Type1")
except FileNotFoundError:
    print("File not found1")
except (NameError, ValueError):
    print("Something wrong1")
print("We started function1")