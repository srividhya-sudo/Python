""" 
TASK: Get the username from the user and generate the userid
For Memory Issues, Limit the userid to length 10 with following conditions
  - if the length of userid is less than 10, then cover it with 0 at prefix
  - if length of userid exceeds 10, then remove the extra characters

For the security reasons, we had to mask the user id with following:
  replace the last two characters with 'X'
Print the userid along with masked userid

Sample Input1:
  nick
Sample Output1:
  000000nick ---- 000000niXX

Sample Input2:
  codewala
Sample Output2:
  00codewala ---- 00codewaXX

Sample Input3:
  SteeveRogers
Sample Output3:
  SteeveRoge ---- SteeveRoXX
"""


def generte_userid(username):
    username = input()
    if len(username) <= 10:
        userid = username.zfill(10)  
    else:
        userid = username[:10] 
    mask_userid = userid[:-2] + 'XX'
    print(f"{userid} ----> {mask_userid}")

generte_userid('')