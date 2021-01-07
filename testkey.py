import shodan
import sys
import time

def test(key):
    api = shodan.Shodan(key)
    print ("{+} Probando Key: %s" %(key))
    try:
        info = api.info()
    except Exception:
        print ("{-} Key %s es invalida  :-( " %(key))
        return False,False
    if info['plan'] == 'dev' or info['plan'] == 'edu' or info['plan'] == 'basic': #this seems to be how they are categorized
        print ("{+} Key %s es valida y de pago :-) !!! " %(key) + " ==>  " + info['plan'])
        return True,True
    elif info['plan'] == 'oss': # however I might be wrong. oh well.
	    print ("{*} Key %s es valida pero gratuita!" %(key))
	    return True,False


def main(args):
    print ("===Shodankeys===")
    if len(args) != 2:
        sys.exit("Shodan API Key List Checker (for testing githubbed keys)\nusage: %s keys-to-test.txt" %(args[0]))
    f = open(args[1], "r")
    keys = f.readlines()
    valid_keys = []
    paid_keys = []
    comm_keys = []
    for key in keys:
        time.sleep(2);#el delay es para dar estabilidad
        key = key.strip()
        is_valid,is_paid = test(key=key)

        try:
            valid_keys.index(key)
        except Exception:
            if is_valid == True:
                valid_keys.append(key)
                if is_paid == True:
                    paid_keys.append(key)
                else:
                    comm_keys.append(key)
            else:
                pass
    print ("\n\n{+} tienes %d keys validas" %(len(valid_keys)))
    print ("{+} tienes %d keys de pago" %(len(paid_keys)))
    print ("{+} tienes %d keys gratuitas" %(len(comm_keys)))
    print ("\n{+} keys de pago...")
    for key in paid_keys:
        print (key)
    print ("\n{+}keys gratuitas...")
    for key in comm_keys:
        print (key)


if __name__ == "__main__":
    main(args=sys.argv)
