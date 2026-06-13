#User input
print("Enter test case count: ")
test_cases=int(input())
print("Enter how many passed: ")
passed_cases=int(input())
print("Enter the total execution time: ")
execution=float(input())
#Calculate and display:
pass_rate=passed_cases / test_cases
fail_rate= (test_cases - passed_cases) / test_cases
avg_time_test= test_cases / execution

def calc_display():
    print(f"Total test cases: {test_cases}\n Pass rate: {pass_rate:.1f}\n Fail rate: {fail_rate:.1f}\n Average time per test: {avg_time_test:.2f}")

calc_display()