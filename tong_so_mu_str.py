import datetime
def sum_pow(base,starter):
    strInput = str(pow(base,starter));
    len_str = len(strInput);
    str_array = [];
    count_str_array = {}
    for i in range(len_str):
                  char = strInput[i];
                  if char in str_array:
                    count_str_array[char] += 1;
                  else:
                    str_array.append(char);
                    count_str_array[char] = 1;
    str_array = {}
    sum_pow = 0
    for str_element in count_str_array:
            sum_pow += int(str_element) * int(count_str_array[str_element])
    print(sum_pow)  
t_start = datetime.datetime.now()
starter = 100
for i in range (13):
        sum_pow(2,starter)
        starter *= 2
t_end = datetime.datetime.now()
print(t_end - t_start)
