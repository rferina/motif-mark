import argparse
import bioinfo
import re
import cairo

def get_args():
    """
    Adds global variables to run different specifications via command line.
    """
    parser = argparse.ArgumentParser(description="Specify parameters")
    parser.add_argument('-f', '--fasta', help='specify FASTA file')
    parser.add_argument('-m', '--motifs', help='specify motif file')
    return parser.parse_args()

# conda activate my_pycairo
# command to run: python motif-mark-oop.py -f test_fa.fasta -m test_motif.txt

args = get_args()

fasta_file = args.fasta
motifs_file = args.motifs

# generate output png filename
png_name = fasta_file.split(".")[0]
png_name = png_name + '.png'



# convert fasta file to one line fasta file
oneline_file = bioinfo.oneline_fasta(fasta_file)
# oneline_file.write()
print('one_line complete')



# with open(oneline_file, 'r') as testing_file:
#     line_count = 0
#     for line in testing_file:
#         line_count +=1
#         line = line.strip('\n')
#         # define gene name as header line
#         if line[0] == '>':
#             print('header')
#         # define start and stop of gene from sequence line
#         elif line[0] != '>':
#             print('seq')

# print('oneline opened')

def create_context(width, height):
    '''Takes in desired width and height, returns the context for drawing.'''
    # create the coordinates to display graphic, desginate output
    surface = cairo.PDFSurface("output.pdf", width, height)
    # create the coordinates to draw on
    context = cairo.Context(surface)
    return surface, context

# create context to draw on
surface, context = create_context(1000, 1200)

# make background white
context.save()
context.set_source_rgb(1, 1, 1)
context.paint()
context.restore()

# context.rectangle(0, 0, 800, 1000)
# context.set_source_rgb(1, 1, 1)
# context.fill()

# need to put in gene function
# context.set_line_width(2)
# context.move_to(100,75)        #(x,y)
# context.line_to(600,75)
# context.stroke()

# # gene name
# # context.set_font_size(0.25)
# context.select_font_face("Arial",
#                      cairo.FONT_SLANT_NORMAL,
#                      cairo.FONT_WEIGHT_NORMAL)
# context.move_to(50, 50)
# context.show_text("Gene 1")

# # exon 
# context.set_line_width(10)
# context.move_to(200,75)        #(x,y)
# context.line_to(300,75)
# context.stroke()

# # motif
# context.set_line_width(25)
# context.set_source_rgba(4, 0, 4, 0.5)
# context.move_to(100,75)        #(x,y)
# context.line_to(105,75)
# context.stroke()

# motif



        
# class Identify:
#     '''Parse clean fasta'''
#     def __init__(self, oneline_fa) -> None:
#         self.oneline_fa = oneline_fa
    
#     def parse_oneline(self):
#         # while loop to read in two lines at a time
#         header_dict = {}
#         while True:
#             header = self.oneline_fa.readline()
#             seq = self.oneline_fa.readline()
#             if not seq: break  
#             # double check header is correct
#             # if header[0] == '<':
#             if header not in header_dict:
#                 header_dict[header] = seq
#         return header_dict


class Gene:
    def __init__(self, oneline_fasta,  gene_start, gene_stop, gene_name, gene_number) -> None:  # gene_start, gene_stop, gene_name
        self.oneline_fa = oneline_fasta
        self.gene_start = gene_start
        self.gene_stop = gene_stop
        self.gene_name = gene_name
        self.gene_number = gene_number
    
    def draw_gene(self):
        # draw gene
        context.set_line_width(2)
        context.set_source_rgba(0, 0, 0)

        if self.gene_number == 1:
            context.move_to(self.gene_start, 75)        #(x,y)
            context.line_to(self.gene_stop, 75)
            context.stroke()
            # add gene name
            context.set_font_size(15)
            context.select_font_face("Arial",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_NORMAL)
            context.move_to(50, 50)
            context.show_text(self.gene_name)
        elif self.gene_number > 1:
            y_val = self.gene_number * 75
            context.move_to(self.gene_start, y_val)        #(x,y)
            context.line_to(self.gene_stop, y_val)
            context.stroke()
            # add gene name
            context.set_font_size(15)
            context.select_font_face("Arial",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_NORMAL)
            context.move_to(50, y_val-25)
            context.show_text(self.gene_name)

    # def draw_gene(self, gene_start, gene_stop, gene_name):

    #     with open(self.oneline_fa, 'r') as fa:
    #         line_count = 0
    #         for line in fa:
    #             line_count +=1
    #             line = line.strip('\n')
    #             # define gene name as header line
    #             if line[0] == '>':
    #                 gene_name = line
    #             # define start and stop of gene from sequence line
    #             elif line[0] != '>':
    #                 # if first character is lowercase, then can assume it's the start pos of the intron
    #                 if line[0].islower() == True:
    #                     gene_start = 0
    #                     if line[-1].islower() == True:
    #                         gene_stop = len(line)

    #     # draw gene
    #     context.set_line_width(2)
    #     context.move_to(gene_start, 75)        #(x,y)
    #     context.line_to(gene_stop, 75)
    #     context.stroke()
    #     # add gene name
    #     context.set_font_size(15)
    #     context.select_font_face("Arial",
    #                  cairo.FONT_SLANT_NORMAL,
    #                  cairo.FONT_WEIGHT_NORMAL)
    #     context.move_to(50, 50)
    #     context.show_text(gene_name)


    # def identify(self, gene_start, gene_stop, gene_name):
    #     # self.gene_start = gene_start
    #     # self.gene_stop = gene_stop
    #     # self.gene_name = gene_name

    #     with open(self.oneline_fa, 'r') as fa:
    #         line_count = 0
    #         for line in fa:
    #             line_count +=1
    #             line = line.strip('\n')
    #             # avoid header lines
    #             if line[0] != '>':
    #                 # if first character is lowercase, then can assume it's the start pos of the intron
    #                 if line[0].islower() == True:
    #                     gene_start = 20
    #                     if line[-1].islower() == True:
    #                         gene_stop = len(line)
    #     return gene_start, gene_stop, gene_name

    # def draw_gene(self):
    #     # NEED TO FIGURE OUT HOW TO CHANGE y of LINE FOR DIFFERENT GENES
    #     # draw gene
    #     context.set_line_width(2)
    #     context.move_to(gene_start, 75)        #(x,y)
    #     context.line_to(gene_stop, 75)
    #     context.stroke()
    #     # add gene name
    #     context.set_font_size(15)
    #     context.select_font_face("Arial",
    #                  cairo.FONT_SLANT_NORMAL,
    #                  cairo.FONT_WEIGHT_NORMAL)
    #     context.move_to(50, 50)
    #     context.show_text(gene_name)


class Exon(Gene):
    def __init__(self, exon_start, exon_stop):
        # super().__init_subclass__ (exon_start, exon_stop):
        """
        Takes in a file path and initializes an
        inverted index (a dictionary) with keys as the
        term and values as the list of documents with
        that term.
        """
        # self.path = path
        self.exon_start = exon_start
        self.exon_stop = exon_stop
    
    # def identify_exon(self):
    #     with open(self, 'r') as fa:
    #         line_count = 0
    #         for line in fa:
    #             line_count +=1
    #             line = line.strip('\n')
    #             # avoid header lines
    #             if line[0] != '>':
    #                 # if first character is lowercase, then can assume it's the start pos of the intron
    #                 if line[0].islower() == True:
    #                     print('yay')

    def draw_exon(self):
        if gene_1.gene_number == 1:
            context.set_line_width(10)
            context.set_source_rgba(0, 0, 0)
            context.move_to(self.exon_start,75)        #(x,y)
            context.line_to(self.exon_stop,75)
            context.stroke()
        elif gene_1.gene_number > 1:
            context.set_line_width(10)
            context.set_source_rgba(0, 0, 0)
            y_val = gene_1.gene_number * 75
            context.move_to(self.exon_start, y_val)        #(x,y)
            context.line_to(self.exon_stop, y_val)
            context.stroke()
#     def identify_exon(self):
#         '''Takes in oneline fasta file, identifies the start and stop positions of the exon.'''
#         with open(self, 'r') as fa:
#             line_count = 0
#             for line in fa:
#                 line_count +=1
#                 line = line.strip('\n')
#                 # avoid header lines
#                 if line[0] != '>':
#                     # if first character is lowercase, then can assume it's the start pos of the intron
#                     if line[0].islower() == True:
#                         print('yay')
#                         left_intron_start = 0
#                         exon = re.search(r'\B[A-Z]\B', line) 
#                         exon_start = exon.start()



# class Line:
#     '''Draws lines'''
#     def __init__(self, start, stop, kind) -> None:
#         self.start = start
#         self.stop = stop
#         self.kind = kind

    # def draw(self, context, y):
	#     '''Takes in context, draw a line on it which represents a gene, exon, motif etc'''
	#     if self.kind == 'gene':
    #         # draw gene from start and stop
    #         print('exon starting at', self.start, 'stop at', self.stop)
            # context.set_line_width(5)
            # context.set_source_rgba(4, 0, 4, 0.5)
            # context.move_to(100,75)        #(x,y)
            # context.line_to(600,75)
            # context.stroke()

            # surface.write_to_png ("gene.png")
		
        # elif self.kind == 'exon':

		# elif self.kind == 'motif'':

class Motif:
    def __init__(self, motif_start, motif_stop) -> None:
        self.motif_start = motif_start
        self.motif_stop = motif_stop

    def draw_motifs(self):
        if gene_1.gene_number == 1:
            context.set_line_width(25)
            context.set_source_rgba(4, 0, 4, 0.5)
            context.move_to(self.motif_start,75)        #(x,y)
            context.line_to(self.motif_stop,75)
            context.stroke()
        elif gene_1.gene_number > 1:
            y_val = gene_1.gene_number * 75
            context.set_line_width(25)
            context.set_source_rgba(4, 0, 4, 0.5)
            context.move_to(self.motif_start, y_val)        #(x,y)
            context.line_to(self.motif_stop, y_val)
            context.stroke()

    # add motifs to dict
    # motifs = []
    # for spec in specs: #specifications 13,19,'motif'
    #     motif= Line(*spec) # explode an array
    #     # store motif obj in list
    #     motifs.append(motif)

    # convert to uppercase
    # motif_option = ''
    # self.motif = self.motif.upper()

    # for nuc in self.motif:
    #     if letter in nuc_dict:
    #         motif_option += nuc_dict[nuc]
    #     # no conversion
    #     else:
    #         motif_option += nuc
    # return motif_option
# list of lists with unique colorsbc rbg lists, append to list, plug list into motifs color 
# opacity .9
# count to add one everytime thru seq, start -1; index motif_count

# list of colors
# start gene obj if not header line


########### RUN STUFF #####################################################################
# mygene = Gene(600, 'gene ayooo')
# mygene.identify()
# mygene.draw_gene()

# mygene = Gene('fa_one_line.fa')
# # mygene = Gene(oneline_file, 100, 600, 'gene1 test')
# mygene.draw_gene(100, 600, 'gene2 test')

# myexon = Exon(200, 300)
# myexon.draw_exon()

# mymotif = Motif(100, 105)
# mymotif.draw_motifs()


# IUPAC dictionary
iupac_dict = {
    "A": "[Aa]",
    "C": "[Cc]",
    "G": "[Gg]",
    "T": "[Tt]",
    "U": "[UuTt]",
    "W": "[AaTtUu]",
    "S": "[CcGg]",
    "M": "[AaCc]",
    "K": "[GgTtUu]",
    "R": "[AaGg]",
    "Y": "[CcTtUu]",
    "B": "[CcGgTt]",
    "D": "[AaGgTtUu]",
    "H": "[AaCcTtUu]",
    "V": "[AaCcGg]",
    "N": "[AaCcGgTtUu]",
    "Z": "[]"
}

# .replace with all

# open motif file
motifs = open(motifs_file, 'r')
line_number = 0
motifs_list = []
for entry in motifs:
    line_number += 1
    entry = entry.strip('\n')
    # translate motif entries if needed
    motif_option = ''
    for nuc in entry:
        if nuc in iupac_dict.keys():
            motif_option += iupac_dict[nuc]
        # no conversion
        else:
            motif_option += nuc
        
    motifs_list.append(motif_option) 
print('motifs list', motifs_list)

# with open, generate Gene obj for each line
testing_file = open('fa_one_line.fa', 'r')
line_count = 0
gene_num = 0
for line in testing_file:
        line_count +=1
        line = line.strip('\n')
        # define gene name as header line
        if line[0] == '>':
            gene_id = line
            gene_id = gene_id.split('>')[1]
        # define start and stop of gene from sequence line
        elif line[0] != '>':
            gene_beg = 100 
            gene_end = len(line) + gene_beg
            gene_num += 1
            # make gene object
            gene_1 = Gene(testing_file, gene_beg, gene_end, gene_id, gene_num)
            print('made obj')
            gene_1.draw_gene()
            print('drew')
            print(gene_1.gene_number)
            # define exon terms
            exon_indexes = []
            for match in re.finditer(r'[A-Z]', line):
                exon_indexes.append(match.start())
                ex_st = exon_indexes[0] + 100
                ex_en = exon_indexes[-1] + 100
                myexon = Exon(ex_st, ex_en)
                myexon.draw_exon()
            print(ex_st, ex_en)
            # look for motifs
            for motif in motifs_list:
                motif_indexes = {}
                motif_list_ind = [] 
                for match in re.finditer(motif, line.upper()):
                    # add motif indexes to a list of tuples to record motifs
                    # being present in sequence lines multiple times
                    motif_list_ind.append((match.start()+100, match.end()+100))
                    # dictionary with key as motif, value as list of tuples of motif indexes
                    if motif not in motif_indexes:
                        motif_indexes[motif] = motif_list_ind
                print(motif_indexes)
                # for motifs on each gene, draw all
                for keys in motif_indexes.keys():
                    if len(motif_indexes[keys]) == 1:
                        motif_count = len(motif_indexes[keys])
                        motif_start = motif_indexes[keys][0][0]
                        motif_stop = motif_indexes[keys][0][1]
                        mymotif = Motif(motif_start, motif_stop)
                        mymotif.draw_motifs()
                    elif len(motif_indexes[keys]) > 1:
                        motif_count = len(motif_indexes[keys])
                        # iterate through the list of tuples in the motif dictionary values
                        for i in range(len(motif_indexes[keys])):
                            motif_start_i = motif_indexes[keys][i][0]
                            motif_stop_i = motif_indexes[keys][i][1]
                            mymotif2 = Motif(motif_start_i, motif_stop_i)
                            mymotif2.draw_motifs()
        
                
      


# complete drawing
surface.write_to_png (png_name)
surface.finish()

testing_file.close()
######################################################################################
# class Exon:
#     def __init__(self, path):
#         """
#         Takes in a file path and initializes an
#         inverted index (a dictionary) with keys as the
#         term and values as the list of documents with
#         that term.
#         """
#         self.path = path

#     def identify_exon(self):
#         '''Takes in oneline fasta file, identifies the start and stop positions of the exon.'''
#         with open(self, 'r') as fa:
#             line_count = 0
#             for line in fa:
#                 line_count +=1
#                 line = line.strip('\n')
#                 # avoid header lines
#                 if line[0] != '>':
#                     # if first character is lowercase, then can assume it's the start pos of the intron
#                     if line[0].islower() == True:
#                         print('yay')
#                         left_intron_start = 0
#                         exon = re.search(r'\B[A-Z]\B', line) 
#                         exon_start = exon.start()





    # def ():
    #     exon_start = Position.()
    #     exon_stop = Position.()

# class Intron:
#     def __init__(self, path):
#         """
#         Takes in a file path and initializes an
#         inverted index (a dictionary) with keys as the
#         term and values as the list of documents with
#         that term.
#         """

# class Motif:
#     def __init__(self, path):
#         """
#         Takes in a file path and initializes an
#         inverted index (a dictionary) with keys as the
#         term and values as the list of documents with
#         that term.
#         """
#     def translate(motif):
#         '''Takes in a motif, and returns motif options if the 
#         motif contains an ambiguous character (y). Otherwise 
#         returns the original motif.'''
        # put variations in list, see if in seq??
        # if line contains something not ACTGU?
        # if line has all caps
        # if motif.isupper() == True:
        #     substitute
        #     findall
        # else: 
        #     motif_up = motif.upper()




##############################################################################################

    # dict with key as captialize, value is set of what it represents; if key in motif look in set
    # {Y:, (C, T)}
    # change y to t or c
    # have regex look for every possibility
    # re.replace()
    # result = re.sub('abc',  'def', input)
#   will have c|t then regex will use that to find it



# notes

# could have diff num of motifs, exons, stick inside list dict or another object
# "gene" 2 
# class FilingCabinet: # dict or obj
#     def __init__(self) -> None:
#         pass
#     def 

# gene1 is a object of type line
# exon1 is object of type line
# fc1=FilingCabinet(gene1, exon1,motifs1) # use * args or a motifs list of line objects motif1a, motif1b; drawn at 300
# fc2=FilingCabinet(gene2, exon2, motifs2, ) # motifs 2 list; drawn at 600
# if do this, in MAIN fcl1.draw(context) fcl2.draw(context) (this is filing cabinet draw, not line draw)

# dif color for each motif type

################## TO DO########################################################################################
# in MAIN 
# parse args
# define classes, functions, constants
# create context
# clean FASTA
# translate ambiguous motifs; make it usable regex; in data structure
# parse clean FASTA file; look for gene (length of seq, store in line obj or filing cabinet), exon (uppercase to identify start/stop stored as line obj),
#        motifs (line obj); need each to belong to a group; not just list; gene names =?? in dict
# draw by looking thru all filing cabinets (collection of filing cabinets in a list)
    # for fc in filing_cabinets:
    #     fc.draw(context)

# for motif1a, motif1b, motif1c
# motifs = []
# for spec in specs: #specifications 13,19,'motif'
#     motif= Line(*spec) # explode an array
#     # store motif obj in list
#     motifs.append(motif)

# len(motifs) should be 3 for this [Line(...), Line(..., Line(...))]
# list of lists

# dict with key
# fasta header can be gene name

# make test input file
# aaaaaAATTAAaaaaa
# motif YY could be TT or CC
# search for all motifs in each gene
# can use random colors for diff motifs; or overlapping motifs stack them (transparent colors?)
# give additional info for second overlapping one, or motifs class to collect all, motifs1.draw can see overlapping

# easy bonus, implement it, make copy of it, change code to implement inheritance just rearranging


# could remove y parameter, instead put in draw method


# # with open(args.fasta, 'r')


# class Shape()
#     pass
# class Circle<Shape: # circle inherits from shape
#     def draw
# class Rectangle<Shape:
#     def draw

# # draw circles in pycairo class

################### old MAIN ###################################################################
# input = 'ygcy'    
# output = input.replace("y", "[c|t]")
# print(output)

# # detect change in case for start of exon
test='aaaBDBcc' # 3-5
# res = re.search(r'\B[A-Z]\B', test) # end not right
# print(res.end()) # start is pos with 0 indexing

# res = [idx for idx in range(len(test)) if test[idx].isupper()]
# print(res)

# res2 = [match.start() for match in re.finditer(r'[A-Z]', test)]
# print(res2[0], res2[-1])
# res3 = []
# for match in re.finditer(r'[A-Z]', test):
#     res3.append(match.start())
#     ex_st = res3[0]
#     ex_en = res3[-1]
# print(ex_st, ex_en)
# print(res3)

# see if case == case at start pos to get end pos?
# res2 = re.finditer(r'\B[A-Z]\B', test) # end not right
# for match in re.finditer(r'\B[A-Z]\B', test):
# #     # print('end', match.end())
#     print("start index", match.start(), "End index", match.end())
    # print(match.group(), "start index", match.start(), "End index", match.end()) # but end of exon is -1


# Position.oneline_fa('Figure_1.fasta')

# # Position.oneline_fa('Figure_1.fasta', 'Figure_1.fasta')

# Exon.identify_exon('fa_one_line.fa')

####################################################################################################


# make exon object from data; could name, throw in dict or list


# class people, each one is a noun; all have a draw functionality
# context obj like piece of paper; white male draws differently
# justine = Person(no hat, brown eyes)
# justine.draw(context object)
# object.draw(context)
##########################################
# if __name__== "__main__":
    # input = 'ygcy'    
    # output = input.replace("y", "[c|t]")
    # print(output)

#     # detect change in case for start of exon
#     test='aaaBDBcc'
#     res = re.search(r'\B[A-Z]\B', test) # end not right
#     print(res.start())
#     # see if case == case at start pos to get end pos?
#     # res2 = re.finditer(r'\B[A-Z]\B', test) # end not right
#     for match in re.finditer(r'\B[A-Z]\B', test):
#         # print('end', match.end())
#         print(match.group(), "start index", match.start(), "End index", match.end()) # but end of exon is -1


#     Position.oneline_fa('Figure_1.fasta')
#     # Position.oneline_fa('Figure_1.fasta', 'Figure_1.fasta')

#     Exon.identify_exon('fa_one_line.fa')

    # file1.oneline_fa()

    # result = re.sub('y', 't', input) 
    # result2 = re.sub('y', 'c', input)

# seq = 'aaaaaaaaCACGGTTGGCACaaaaa'
# mot_test = ['CAC', 'TT']
# for m in mot_test:
#     mot_indexes = {}
#     mot_list = []
#     for match in re.finditer(m, seq):
#         mot_list.append((match.start()+100, match.end()+100))
#         if m not in mot_indexes:
#             mot_indexes[m] = mot_list
#     print(mot_indexes)


# newObject = originalString.replace('character to replace', 'character to be replaced with, count of replacements to perform)

# append all instances to list, then put list as dict val