import re

sample_inputs = [
    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>

    This URL is not inside a hyperlink tag, so should be ignored: "http://www.google.com"
    """,
    
    """
    This is almost a hyperlink, but the quotes are mismatched, so it shouldn't be captured:

    <a href="http://www.google.com/super_secret/all_the_user_data/'>Please don't click</a>

    <a href="http://www.google.com/super_secret/user_data/'>Please don't click</a>


    
    """,

    
]

sample_inputs = [
    """
    This is a long string
    without an email address
    It is what it is
    """,


    """
    This string has an email!
    karl@erik.no
    (don't expect replies!)
    """,
    
    """
    Here is an email:simon@funke.no. It's probably not going to work.
    You could try funsim@uio.no, but I don't think that's the right one either. 
    """,

    """
    This is a bit of html:
	<span id="vrtx-person-change-language-link">
	  <a href="http://www.mn.uio.no/ifi/personer/vit/karleh/index.html">Norwegian<span class="offscreen-screenreader"> version of this page</span></a>
	</span>

        
          
            <div class="vrtx-person-contact-info-line vrtx-email"><span class="vrtx-label">Email</span>
              
                <a class="vrtx-value" href="mailto:karleh@ifi.uio.no">karleh@ifi.uio.no</a>
              
            </div>
    """,

    """This is text which contains some email-like strings which aren't emails 
    according to the definition of the assignment:
    the string name@server.1o has a number at the start of thedomain,
    the string name@server.o1 has a number at the end,
    the string name@ser<ver.domin has an illegal character in its server,
    as does the string name@ser"ver.domain,

    however, the string na&me@domain.com is actually an email!
    as is n~ame@dom_ain.com
    but name@domain._com is bad
    (name@domain.c_o.uk is allowed though)
    """
]
#isalnum()
# .#$%&~’*+-/=? ‘|{}
#NAME@SERVER
#if '.' or '#' or '$' or '%' or '&' or '~' or '’' or '*' or '+' or '-' or '/' or '=' or '?' or '_' or '‘' or '|' or '{' or '}' in values2[j]:
# sentence.count('a')
#special_char_list=['.','#','$','%','&','~','’','*','+','-','/','=','?','_','‘','|','{','}']
special_char_list=['#','$','%','&','~','’','*','+','-','/','=','?','_','‘','|','{','}']

def return_domain(string):
	index_of_last_period=0
	for i in range(0,len(string)):
		reverse_index=len(string)-i-1
		##print (h[reverse_index])
		if string[reverse_index]=='.':
			index_of_last_period=reverse_index
			break;
	for i in range(index_of_last_period+1,len(string)):
		if i==index_of_last_period+1:
			domain_string=string[i]
			continue;
		##print ("ll",h[i])
		domain_string=domain_string+string[i]
	return domain_string


def find_emails(text):
	validemails=[]

	for line in text:
		values1 = re.split(' ', line);
		##print (line)
		for i in range(0,len(values1)):
			if '@' in values1[i]:
				#print ("has @ in it",values1[i])
				values2 = re.split('@|\n|<|>', values1[i]);
				#values2 = re.split('@|\n', values1[i]);

				#print ("split up @",values2)
				validparts=[]
##########################################################################
				for j in range(0,len(values2)):
					if ':' in values2[j]:
						values2temp1 = re.split(':', values2[j]);
						values2[j]=values2temp1[1]
						#print ("di it", values2[j],values2)
##########################################################################
					for j in range(0,len(values2)):
						if len(values2[j])>0:
							##print ("caught one",values2[j],values2[j][-1])
							if values2[j][-1]==',' or values2[j][-1]=='.'or values2[j][-1]=='"':
								values2[j]=values2[j][:-1]
							if values2[j][0]=='(':
								values2[j]=values2[j][1:]
##########################################################################

				for j in range(0,len(values2)):

					for k in range(0, len(special_char_list)):
						if special_char_list[k] in values2[j]:
							special_char_count=values2[j].count(special_char_list[k])
							if special_char_count==1:
								#print ("possibly valid",values2[j])
								values2temp = values2[j].replace(special_char_list[k],'')
								values2temp2 = values2temp.replace('.','')
								#print ("here", values2temp2)
								if values2temp2.isalnum():
									##print ("valid", values2[j])
									validparts.append(values2[j])
									break;

					values2temp = values2[j].replace('.','')
					#print ("erhere",values2temp)
					if values2temp.isalnum():
						#print("alphanumeric",values2[j])
						validparts.append(values2[j])
				#print("validparts",validparts)

				for i in range(0,int(len(validparts)/2)):
					#print ("return domain", return_domain(validparts[(i*2)+1]))
					if return_domain(validparts[(i*2)+1]).isalpha():
						#print ("Yesy")
						if '.' in validparts[(i*2)+1]:
							validemails.append(validparts[i*2]+'@'+validparts[(i*2)+1])

	return validemails

print (find_emails(sample_inputs))


expected_outputs = [
    [],
    ["karl@erik.no"],
    ["simon@funke.no", "funsim@uio.no"],
    ["karleh@ifi.uio.no", "karleh@ifi.uio.no"],
    ["na&me@domain.com", "n~ame@dom_ain.com", "name@domain.c_o.uk"]
    
]

def find_ahref(text):
	links=[]

	for line in text:
		try:
			#print ("new line", line)
			if '<a href' in line:
				values1 = re.split(' |=|>', line);
				#print ("values1",values1)

				link=[]
				if len(values1)>2:
					for i in range(0, len(values1)-2):
						if values1[i]=='<a' and values1[i+1]=='href':
							#print("values1",values1[i],values1[i+1])
							on=1
							link.append(values1[i+2])
				links.append(link)
		except TypeError:
			pass
	#print (links)
	return(links)

#print ("kk",(find_ahref(sample_inputs)))

def check_enclosing_quotes(list_of_links):
	linklist=[]
	for i in range(0, len(list_of_links)):
		for j in range(0,len(list_of_links[i])):
			#print ("lll",list_of_links[i][j][0],list_of_links[i][j][len(list_of_links[i][j])-1])
			if list_of_links[i][j][0]==list_of_links[i][j][len(list_of_links[i][j])-1]:
				#print ("yes1",list_of_links[i][j])
				linklist.append(list_of_links[i][j][1:-1])

				#return list_of_links[i][j][1:-1]
	return linklist

#print(check_enclosing_quotes(find_ahref(sample_inputs)))

def extract_protocol(link_without_quotes):
	protocol=''
	try:
		for i in range(0, len(link_without_quotes)):
			#print (link_without_quotes[i])
			if link_without_quotes[i]==':':
				break;
			protocol=protocol+link_without_quotes[i]
		return protocol
	except TypeError:
		return protocol


#print (extract_protocol(check_enclosing_quotes(find_ahref(sample_inputs))))

def extract_host_and_domain(link_without_quotes):
	hostanddomain=''
	on=0
	try:
		if len(link_without_quotes)>=2:
			for i in range(0, len(link_without_quotes)):
			#print (link_without_quotes[i])

				#if on==1 and link_without_quotes[i]=='/' and link_without_quotes[i-1]!='/':
				#	break;

				#if link_without_quotes[i]=='/' and link_without_quotes[i-1]!='/' and link_without_quotes[i+1]!='/':
				#	break;
				if on==1:
					hostanddomain=hostanddomain+link_without_quotes[i]
				if link_without_quotes[i]=='/' and link_without_quotes[i-1]=='/':
					on=1

			return hostanddomain
	except TypeError:

			return hostanddomain

#print (extract_host_and_domain(check_enclosing_quotes(find_ahref(sample_inputs))))

def extract_path(link_without_quotes):
	path=''
	on=0
	try:
		if len(link_without_quotes)>=2:
			print (link_without_quotes)
			for i in range(0, len(link_without_quotes)):
				print (len(link_without_quotes))
				print (i,"kkk",link_without_quotes[i],link_without_quotes[i-1])
				if on==1:
					path=path+link_without_quotes[i]
				print ("kkk",link_without_quotes[i],link_without_quotes[i-1])
				#if link_without_quotes[i]=='/' and link_without_quotes[i-1]!='/' and link_without_quotes[i+1]!='/':
				if link_without_quotes[i]=='/' and link_without_quotes[i-1]!='/' and i==(len(link_without_quotes)-1):
					print("jjjjjj",link_without_quotes[i])
					print(i,len(link_without_quotes[i-1]))
					on=1;

		return path

	except TypeError:
		print ("found error")
		return path

#print (extract_path(check_enclosing_quotes(find_ahref(sample_inputs))))

def find_urls(text):
	#print (check_enclosing_quotes(find_ahref(text)))

	l=check_enclosing_quotes(find_ahref(text))
	l_temp=[]
	for z in range(0,len(l)):

		#print(extract_protocol(l[z]))
		if extract_protocol(l[z])=='http' or extract_protocol(l[z])=='https':
			l_temp.append(l[z])

	l=l_temp

	#print ("l", l)

	l_temp=[]

	for z in range(0,len(l)):
		#print ("here",z,l[z])
		#print(extract_host_and_domain(l[z]))
		ltemp=extract_host_and_domain(l[z]).replace('.','')
		ltemp2=ltemp.replace('-','')
		ltemp3=ltemp2.replace('/','')
		ltemp4=ltemp3.replace('~','')
		if ltemp4.isalnum():
			l_temp.append(l[z])

	l=l_temp

	#print ("l3", l)
	return l


print ("test sample",find_urls(sample_inputs))

