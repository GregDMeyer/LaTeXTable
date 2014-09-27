from Tkinter import *
import sys

usage = '''
USAGE:

python LaTeXtable.py -r [number of rows] -c [number of columns]

Enjoy!
'''

class GUI(object):

	def __init__(self,master,nrow,ncol):

		self.master = master

		self.nrow = nrow
		self.ncol = ncol

		self.topframe = Frame(self.master)
		self.topframe.pack(padx=10,pady=10)

		self.frame1 = Frame(self.topframe,highlightbackground='gray1',highlightcolor='gray1',highlightthickness=1)
		self.frame1.pack()

		self.frame2 = Frame(self.topframe,highlightbackground='gray1',highlightcolor='gray1',highlightthickness=1)
		self.frame2.pack()

		self.entries = []

		for i in xrange(ncol):

			self.entries.append([])
			pass

		for j in xrange(nrow):

			for i in xrange(ncol):

				if not j:
					self.entries[i].append( Entry( self.frame1 ) )
				else:
					self.entries[i].append( Entry( self.frame2 ) )
				self.entries[i][j].grid(row=j,column=i)

				pass

			pass

		self.bottomframe = Frame(self.master)
		self.bottomframe.grid_columnconfigure(1,weight=1)
		self.bottomframe.pack(padx=10,pady=10,fill='x',expand=True)

		self.captionLabel = Label( self.bottomframe, text='Caption:')
		self.captionLabel.grid(column=0,row=0)

		self.captionEntry = Entry( self.bottomframe)
		self.captionEntry.grid(column=1,row=0,sticky='EW')

		self.goButton = Button(self.bottomframe,text='Generate LaTeX',command=self.pullTrigger)
		self.goButton.grid(row=1,columnspan=2,stick='EW')

		pass

	def pullTrigger(self,event=None):

		columntitles = []

		for i in xrange(ncol):

			columntitles.append( self.entries[i][0].get() )

		data = {}

		for i in xrange(ncol):

			data[ columntitles[i] ] = []

			for j in xrange(1,nrow):

				data[ columntitles[i] ].append( self.entries[i][j].get() )
				pass

			pass

		cap = self.captionEntry.get()

		colsetup = 'c|'*self.ncol

		firstrow = ''
		rows = ''
		for i in xrange(len(columntitles)):
			if i: 
				firstrow += ' & '
				pass
			firstrow += columntitles[i]

		firstrow += ' \\\\ \\hline'

		#do other rows
		for j in xrange( len( data[columntitles[0]] ) ):
			if j: 
				rows += '''
		'''
				pass
			for i in xrange(len(columntitles)):
				if i:
					rows += ' & '
					pass
				rows += data[columntitles[i]][j]
				pass
			rows += ' \\\\'
			pass


		output = '''
\\begin{table}
	\\centering
	\\begin{tabular}{|'''+colsetup+'''}
		\\hline
		'''+firstrow+'''
		'''+rows+'''
		\\hline
	\\end{tabular}'''

		if cap:
			output+='''
	\\caption{'''+cap+'''}'''

		output+='''
\\end{table}
'''

		print output

		pass

ncol = None
nrow = None

for arg_n in xrange( len(sys.argv) ):

	if sys.argv[arg_n] == '-c':
		ncol = int(sys.argv[arg_n+1])
		pass
	elif sys.argv[arg_n] == '-r':
		nrow = int(sys.argv[arg_n+1])
		pass

	pass

if not all([ncol,nrow]):
	print usage
	sys.exit()

root = Tk()

app = GUI( root, nrow, ncol )

root.mainloop()



# firstrow = ''
# rows = ''
# for i in xrange(len(columntitles)):
# 	if i: 
# 		firstrow += ' & '
# 		pass
# 	firstrow += columntitles[i]

# firstrow += ' \\\\ \\hline'

# #do other rows
# for j in xrange( len( data[columntitles[0]] ) ):
# 	if j: 
# 		rows += '''
# 		'''
# 		pass
# 	for i in xrange(len(columntitles)):
# 		if i:
# 			rows += ' & '
# 			pass
# 		rows += data[columntitles[i]][j]
# 		pass
# 	rows += ' \\\\'
# 	pass


# output = '''
# \\begin{table}
# 	\\centering
# 	\\begin{tabular}{|'''+colsetup+'''}
# 		\\hline
# 		'''+firstrow+'''
# 		'''+rows+'''
# 		\\hline
# 	\\end{tabular}'''

# if cap:
# 	output+='''
# 	\\caption{'''+cap+'''}'''

# output+='''
# \\end{table}
# '''

# print output

# '''