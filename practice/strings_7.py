a = "venkat"
b = 'chandu'
c =  """prasad"""
d = '''balaji'''


"""
indexing
     "python"
      012345
     -6-5-4-3-2-1
 """
print(f"Positive {b[2]}")
print(f"Negative {b[-4]}")

# multi line string(using \,""")
sentence = 'This \
is python \
prime batch'
print(sentence)

# concatenation
name = "john"
_id = 1002
password = name + "_" + str(_id)

print(password.capitalize())

news = "తాజా వార్తలు మరియు బ్రేకింగ్ న్యూస్ ఆంధ్రప్రదేశ్, తెలంగాణ, రాజకీయాలు, జాతీయం, రాష్ట్రం, ప్రపంచం, అంతర్జాతీయం,టీవీ, సినిమా, క్రీడలు, వ్యాపారం,"
sans = "किसी भी प्रकार की नई "
print(news[-1], sans)
