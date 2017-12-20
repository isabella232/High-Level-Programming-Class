# coding=utf8

test_str = ("This is some Nwodkram text. Note that *this* is in italic, and %this% is in bold.\n"
            "If you want to write an \\* or an equal sign and not have the parser eat them, \n"
            "that's easy -  note that \\* this \\* is not in italic even though it's between two \\*s,\n"
            "and \\% this \\% is not in bold.\n\n"
            "[here](www.google.com) is a hyperlink.\n"
            "[here](http://www.google.com) is another.\n"
            "[and here](https://www.weird?$|site.weird/path/) is a third with some weird characters.\n"
            "Follow it at your own peril.\n\n"
            "Ideally, it would be good if your <imageURL>(w=22,h=56) hyperlinks can contain parentheses and underscores.\n"
            "<< But don't worry too much if some weird combination is ambiguous or results in\n"
            "weird stuff. [wp:bird]")

def findandreplace_italic(text):

	on=0
	for i in range(0, len(text)):
		##print (text[i],end='')

		if on==1 and text[i]=='*':
			italic_word=''.join(italic)
			text=text.replace('*'+italic_word+'*','<i>'+italic_word+'</i>')

			on=0
			continue

		if on==1:
			italic.append(text[i])

		if on!=1 and text[i]=='*':
			if text[i-1]!='\\':
				if text[i-2]!='\\':
					italic=[]
					##print ("got one")
					on=1
	return text



##print(findandreplace_italic(test_str))


def findandreplace_bold(text):

	on=0
	for i in range(0, len(text)):
		##print (text[i],end='')

		if on==1 and text[i]=='%':
			bold_word=''.join(bold)
			text=text.replace('%'+bold_word+'%','<b>'+bold_word+'</b>')
			on=0
			continue

		if on==1:
			bold.append(text[i])

		if on!=1 and text[i]=='%':
			if text[i-1]!='\\':
				if text[i-2]!='\\':
					bold=[]
					##print ("got one")
					on=1
	return text

##print(findandreplace_bold(test_str))

def findandreplace_hyperlink(text):

	on=0
	begin=0
	for i in range(0, len(text)):

		if text[i]=='[':
			begin=1
			link=[]
			continue

		if text[i]==']' and begin==1:
			begin=2
		##print (text[i],end='')
		if begin==1:
			link.append(text[i])

		if on==1 and text[i]==')' and begin==2:
			hyperlink_word=''.join(hyperlink)
			begin_word=''.join(link)
			if 'http' not in hyperlink_word:
				hyperlink_word2='http://'+hyperlink_word
			if 'http' in hyperlink_word:
				hyperlink_word2=hyperlink_word
			text=text.replace('['+begin_word+']('+hyperlink_word+')','<a href=\"'+hyperlink_word2+'\">'+begin_word +'</a>')
			on=0
			continue

		if on==1 and begin==2:
			hyperlink.append(text[i])

		if on!=1 and text[i]=='(' and begin==2:
				hyperlink=[]
				##print ("got one")
				on=1
	return text

##print(findandreplace_hyperlink(test_str))
# <imageURL>(w=WIDTH,h=HEIGHT)
# <img src="smiley.gif" alt="Smiley face" height="42" width="42"> 
#<img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="W3Schools.com"> 

def findandreplace_image(text):

	on=0
	on2=0
	for i in range(0, len(text)):
		##print (text[i],end='')

		if on==1 and text[i]=='=' and text[i-1]=='h':
			on2=1
			on=0
			continue



		if on2==1 and text[i]==')':

			height_word=''.join(height)
			width_word=''.join(width)
			imagesrc_word=''.join(imagesrc)
			#print (width_word)
			#print (height_word)
			#print ('<'+imagesrc_word+'>(w='+width_word+',h='+height_word+')')
			text=text.replace('<'+imagesrc_word+'>(w='+width_word+',h='+height_word+')','<img src="'+imagesrc_word+'" height="'+height_word+'" width="'+width_word+'">')
			on=0
			on2=0
			continue

		if on2==1:
			height.append(text[i])

		if on==1 and text[i]!=',' and text[i]!='h':
			width.append(text[i])

		if on!=1 and text[i]=='=' and text[i-1]=='w' and text[i-2]=='(' and text[i-3]=='>' :
				width=[]
				height=[]
				imagesrc=[]
				on=1
				#print ("imh ere")

				for j in range(4, i):
					textback=text[i-j]
					if textback=='<':
						imagesrc.reverse()
						break;
					imagesrc.append(textback)

	return text

##print(findandreplace_image(test_str))


def findandreplace_quotes(text):
	on=0
	for i in range(0, len(text)):
		#print (text[i])

		if on==1 and text[i]=='.':
			quote_word=''.join(quote)
			text=text.replace('<<'+quote_word,'<blockquote>'+quote_word+'</blockquote>')
			on=0
			continue

		if on==1:
			quote.append(text[i])

		if on!=1 and text[i]=='<' and text[i-1]=='<':
				#print ("yesy")

				quote=[]

				on=1
	return text

##print ("here2",findandreplace_quotes(test_str))

def findandreplace_wikipediasearch(text):

	on=0
	for i in range(0, len(text)):
		##print (text[i],end='')

		if on==1 and text[i]==']':
			wp_word=''.join(wp)
			text=text.replace('[wp:'+wp_word+']','https://en.wikipedia.org/wiki/'+wp_word)
			on=0
			continue

		if on==1:
			wp.append(text[i])

		if on!=1 and text[i]==':' and text[i-1]=='p' and text[i-2]=='w' and text[i-3]=='[':

				wp=[]

				on=1
	return text

##print (findandreplace_wikipediasearch(test_str))

def parse_nwodkram(text):

	return findandreplace_wikipediasearch(findandreplace_quotes(findandreplace_image(findandreplace_hyperlink(findandreplace_italic(findandreplace_bold(text))))))

print (parse_nwodkram(test_str))



