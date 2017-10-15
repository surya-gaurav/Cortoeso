import string, random

def generate_short_code(size = 6, chars = string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def create_short_code(instance, size = 6):
	code = generate_short_code(size = 6)
	Short_URL = instance.__class__
	ob_exist = Short_URL.objects.filter(short_url = code).exists()
	if ob_exist:
		return create_short_code(instance, size = 6)
	return code
	