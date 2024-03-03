driving = input('請問您有開過車嗎? ')
if driving != '有' and driving != '沒有':
	print('只能回答 有/沒有 喔')
	raise SystemExit

age = input('請問您的年齡: ')
i_age = int(age)
if driving == '有':
	if i_age >= 18:
		print('已通過測驗')
	else:
		print('請問您怎麼會有開過車?')
elif driving == '沒有':
	if i_age >= 18:
		print('您已經可以考駕照了喔!')
	else:
		print('要等到18歲才能考駕照開車喔!')