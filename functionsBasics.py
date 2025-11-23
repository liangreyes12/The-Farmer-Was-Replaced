while True:
	if can_harvest():
		change_hat(Hats.Green_Hat)
		harvest()
	else:
		change_hat(Hats.Brown_Hat)
		pet_the_piggy()