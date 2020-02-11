from state import State
from functools import reduce
def main(N):
    new_state = State(N)
    new_state.print()


if __name__ == "__main__":
    while True:
        N_val = input("What dimension would you like to use?\n")
        try:
            N_val = int(N_val)
            if N_val <= 0 or N_val > 9:
                raise ValueError
            else:
                break
        except ValueError:
            print("N value must be between 0 and 20\nTry Again\n")
        except:
            print("N value must be an integer\nTry Again\n")
    main(N_val)