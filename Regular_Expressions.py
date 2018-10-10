#Exemplo
# Um programa capaz de fazer matching de um input de um email 
# Por exemplo python-list@python.org Basta introduzer esse mesmo input
import re

pattern = re.compile(r"\[on|off]")
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50db] [on]"))

print(re.search(pattern, "Nada...:-("))

def test_email(your_pattern):
	pattern = re.compile(your_pattern)
	emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
	for email in emails: 
		if not re.match(pattern,email):
			print("You failed to match %s" % email)
		elif not your_pattern:
			print("Forgot to enter a pattern!")
		else: 
			print("Pass")

#Existem dois tipos de input o "input" normal e o "raw_input" aqui como usamos o @ tem de ser com "raw_input"
x = raw_input("Please introduce your pattern for an e-mail:  ")
your_pattern = "r"+x
test_email(your_pattern)