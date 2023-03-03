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

# convert fasta file to one line fasta file
oneline_file = bioinfo.oneline_fasta(fasta_file)
print('one_line complete')


def create_context(width, height):
    '''Takes in desired width and height, returns the context for drawing.'''
    # create the coordinates to display your graphic, desginate output
    surface = cairo.PDFSurface("output.pdf", width, height)
    # create the coordinates you will be drawing on (like a transparency) - you can create a transformation matrix
    context = cairo.Context(surface)
    return surface, context

surface, context = create_context(800, 1000)


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



        
class Identify:
    '''Parse clean fasta'''
    def __init__(self, oneline_fa) -> None:
        self.oneline_fa = oneline_fa
    
    def parse_oneline(self):
        # while loop to read in two lines at a time
        header_dict = {}
        while True:
            header = self.oneline_fa.readline()
            seq = self.oneline_fa.readline()
            if not seq: break  
            # double check header is correct
            # if header[0] == '<':
            if header not in header_dict:
                header_dict[header] = seq
        return header_dict


class Gene:
    def __init__(self, oneline_fa, gene_start, gene_stop, gene_name) -> None:
        self.oneline_fa = oneline_fa
        self.gene_start = gene_start
        self.gene_stop = gene_stop
        self.gene_name = gene_name
     

    def identify(self):
        with open(self, 'r') as fa:
            line_count = 0
            for line in fa:
                line_count +=1
                line = line.strip('\n')
                # avoid header lines
                if line[0] != '>':
                    # if first character is lowercase, then can assume it's the start pos of the intron
                    if line[0].islower() == True:
                        self.gene_start = 20
                        if line[-1].islower() == True:
                            self.gene_stop = len(line)
        return self.gene_start, self.gene_stop

    def draw_gene(self):
        # NEED TO FIGURE OUT HOW TO CHANGE y of LINE FOR DIFFERENT GENES
        # draw gene
        context.set_line_width(2)
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
    
    def identify_exon(self):
        with open(self, 'r') as fa:
            line_count = 0
            for line in fa:
                line_count +=1
                line = line.strip('\n')
                # avoid header lines
                if line[0] != '>':
                    # if first character is lowercase, then can assume it's the start pos of the intron
                    if line[0].islower() == True:
                        print('yay')

    def draw_exon(self):
        context.set_line_width(10)
        context.move_to(self.exon_start,75)        #(x,y)
        context.line_to(self.exon_stop,75)
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
        context.set_line_width(25)
        context.set_source_rgba(4, 0, 4, 0.5)
        context.move_to(self.motif_start,75)        #(x,y)
        context.line_to(self.motif_stop,75)
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


# list of colors
# start gene obj if not header line


########### RUN STUFF #####################################################################
# Position(fasta_file)
mygene = Gene(600, 'gene ayooo')
mygene.identify()
mygene.draw_gene()

myexon = Exon(200, 300)
myexon.draw_exon()

mymotif = Motif(100, 105)
mymotif.draw_motifs()

# print(Identify(oneline_file))
# print('identified')

surface.write_to_png ("gene_test.png")

surface.finish()


# with open, generate Gene obj for each line
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
# test='aaaBDBcc'
# res = re.search(r'\B[A-Z]\B', test) # end not right
# print(res.start())
# # see if case == case at start pos to get end pos?
# # res2 = re.finditer(r'\B[A-Z]\B', test) # end not right
# for match in re.finditer(r'\B[A-Z]\B', test):
#     # print('end', match.end())
#     print(match.group(), "start index", match.start(), "End index", match.end()) # but end of exon is -1


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



# newObject = originalString.replace('character to replace', 'character to be replaced with, count of replacements to perform)



#  def bioinfo.oneline_fasta(file):
        # '''Makes FASTA sequences on one line. Writes out to the file
        # fa_one_line.fa. Returns the number of records so they can be
        # manually compared to the number of header lines in the output file,
        # to confirm the output file is accurate.'''
        # # make dict with headers as keys and sequences as values
        # seq_dict = {}
        # with open(file, 'r') as fa:
        #     line_count = 0
        #     for line in fa:
        #         line_count +=1
        #         line = line.strip('\n')
        #         # only get header lines
        #         if line[0] == '>':
        #             header_line = line
        #         # populate dict with seq lines (non-header lines)
        #         else:    
        #             if header_line not in seq_dict:
        #                 seq_dict[header_line] = line
        #             else:
        #                 seq_dict[header_line] += line
        # # write out to file
        # fa_one_line = open('fa_one_line.fa', 'w')
        # for keys,vals in seq_dict.items():
        #     fa_one_line.write(str(keys) + '\n' + str(vals) + '\n')
        # fa_one_line.close()
        # return len(seq_dict)