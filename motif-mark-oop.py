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


args = get_args()

fasta_file = args.fasta
motifs_file = args.motifs

# generate output png filename
png_name = fasta_file.split(".")[0]
png_name = png_name + '.png'

# convert fasta file to one line fasta file
oneline_file = bioinfo.oneline_fasta(fasta_file)

def create_context(width, height):
    '''Takes in desired width and height, returns the surface and context for pycairo drawing.'''
    # create the coordinates to display graphic, desginate output
    surface = cairo.PDFSurface("output.pdf", width, height)
    # create the coordinates to draw on
    context = cairo.Context(surface)
    return surface, context

# create context to draw on
surface, context = create_context(1300, 1200)

# make background white
context.save()
context.set_source_rgb(1, 1, 1)
context.paint()
context.restore()

# add title to figure
context.set_font_size(15)
context.select_font_face("Arial",
            cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
context.move_to(500, 20)
context.show_text('Motif Marker Visualizer')

# make legend
context.set_font_size(13)
context.select_font_face("Arial",
            cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
context.move_to(1115, 25)
context.show_text('Legend')

# legend intron label
context.set_line_width(2)
context.set_source_rgba(0, 0, 0)
context.move_to(1115, 50)        #(x,y)
context.line_to(1125, 50)
context.stroke()
context.set_font_size(10)
context.select_font_face("Arial",
            cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
context.move_to(1130, 50)
context.show_text('Intron')

# legend exon label
context.set_line_width(10)
context.set_source_rgba(0, 0, 0)
context.move_to(1115, 75)        #(x,y)
context.line_to(1125, 75)
context.stroke()
context.set_font_size(10)
context.select_font_face("Arial",
            cairo.FONT_SLANT_NORMAL,
            cairo.FONT_WEIGHT_NORMAL)
context.move_to(1130, 75)
context.show_text('Exon')

# define colors for motifs
colors = [[0, 1, 1, 0.8], [0.75, 0.24, 1, 0.8], [0, 0, 1, 0.8],
           [0.41, 0.55, 0.13, 0.8], [1, 0.27, 0, 0.8], [0.2, 0.63, 0.79, 0.8]]


class Gene:
    '''This class represents a gene's sequence from a FASTA file. It has a method to draw the
    gene to scale via Pycairo, and the gene name is also recorded on the drawing.
    '''
    def __init__(self, oneline_fasta, gene_start, gene_stop, gene_name, gene_number) -> None:  
        '''Takes in a fasta file where each sequence is on one line. Also takes in and intializes the index
        of where the gene starts and stops, as well as the gene name, and gene number (gene number
        corresponds to a sequence line in the fasta file.)'''
        self.oneline_fa = oneline_fasta
        self.gene_start = gene_start
        self.gene_stop = gene_stop
        self.gene_name = gene_name
        self.gene_number = gene_number
    
    def draw_gene(self):
        '''Returns the gene drawing with gene name.'''
        # set line width, black color
        context.set_line_width(2)
        context.set_source_rgba(0, 0, 0)
        # draw first gene from fasta file
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
        # draw subsequent genes from fasta file, adjusting for the y value
        # of where they'll be drawn
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


class Exon:
    '''This class represents the casette exon present in the FASTA file sequence. It has a method
    to draw the exon to scale via Pycairo.
    '''
    def __init__(self, exon_start, exon_stop):
        """Takes in and initializes the exon start and stop positions."""
        self.exon_start = exon_start
        self.exon_stop = exon_stop

    def draw_exon(self):
        '''Returns the exon drawing.'''
        # set line width, black color
        context.set_line_width(10)
        context.set_source_rgba(0, 0, 0)
        # draw exon associated with first gene from fasta file
        if gene_1.gene_number == 1:
            context.move_to(self.exon_start, 75)        #(x,y)
            context.line_to(self.exon_stop, 75)
            context.stroke()
        # draw exons associated with subsequent genes from fasta file, adjusting for the y value
        # of where they'll be drawn
        elif gene_1.gene_number > 1:
            y_val = gene_1.gene_number * 75
            context.move_to(self.exon_start, y_val)        #(x,y)
            context.line_to(self.exon_stop, y_val)
            context.stroke()


class Motif:
    '''This class represents the motifs that can be found in a gene's sequence in a FASTA file. It has a method to draw
    the motifs to scale via Pycairo, with unique colors for each motif.'''
    def __init__(self, motif_start, motif_stop, m_color) -> None:
        '''Takes in and initializes the motif start and stop positions, as well as unique color for the motif.'''
        self.motif_start = motif_start
        self.motif_stop = motif_stop
        self.m_color = m_color

    def draw_motifs(self):
        '''Returns the motifs drawing.'''
        motif_count = 0
        if gene_1.gene_number == 1:
            motif_count += 1
            context.set_line_width(25)
            context.set_source_rgba(self.m_color[0], self.m_color[1], self.m_color[2], self.m_color[3])
            context.move_to(self.motif_start, 75)        #(x,y)
            context.line_to(self.motif_stop, 75)
            context.stroke()
        elif gene_1.gene_number > 1:
            motif_count += 1
            y_val = gene_1.gene_number * 75
            context.set_line_width(25)
            context.set_source_rgba(self.m_color[0], self.m_color[1], self.m_color[2], self.m_color[3])
            context.move_to(self.motif_start, y_val)        #(x,y)
            context.line_to(self.motif_stop, y_val)
            context.stroke()


# IUPAC dictionary for ambiguous motifs
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

# list of y values to draw motif legend
y_list = [100, 125, 150, 175, 200, 225]

# open motif file, generate list of possible motifs
motifs = open(motifs_file, 'r')
line_number = 0
motifs_list = []
untranslated_motif_list = []
for entry in motifs:
    line_number += 1
    entry = entry.strip('\n')
    # make untranslated motif list to later label motifs in the legend
    untranslated_motif_list.append(entry)
    # make motifs uppercase to check if they're in ipauc diciontary
    entry = entry.upper()
    # translate ambiguous motif entries if needed
    motif_option = ''
    for nuc in entry:
        if nuc in iupac_dict.keys():
            motif_option += iupac_dict[nuc]
        # if translation not needed
        else:
            motif_option += nuc   
    motifs_list.append(motif_option) 

# open one line fasta file, generate Gene object for each sequence line
fasta_one_line_file = open('fa_one_line.fa', 'r')
line_count = 0
gene_num = 0
for line in fasta_one_line_file:
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
            # gene number keeps track of what gene the file is on
            gene_num += 1
            # make gene object for each sequence line, draw genes
            gene_1 = Gene(fasta_one_line_file, gene_beg, gene_end, gene_id, gene_num)
            gene_1.draw_gene()
            # identify start and stop positions of exons 
            exon_indexes = []
            for match in re.finditer(r'[A-Z]', line):
                exon_indexes.append(match.start())
                ex_start = exon_indexes[0] + 100
                ex_end = exon_indexes[-1] + 100
                # generate Exon objects and draw them
                myexon = Exon(ex_start, ex_end)
                myexon.draw_exon()
            # look for motifs in the sequence lines
            for motif, color, y_value, normal_motif in zip(motifs_list, colors, y_list, untranslated_motif_list):
                motif_indexes = {}
                motif_list_ind = []
                for match in re.finditer(motif, line.upper()):
                    # add motif indexes to a list of tuples to record motifs
                    # being present in sequence lines multiple times
                    motif_list_ind.append((match.start()+100, match.end()+100))
                    # dictionary with key as motif, value as list of tuples of motif indexes
                    if motif not in motif_indexes:
                        motif_indexes[motif] = motif_list_ind
                # for motifs on each gene, draw all the motifs
                for keys in motif_indexes.keys():
                    # motif count is how many instances there are of one motif
                    motif_count = len(motif_indexes[keys])
                    # if there's only one instance of the motif
                    if motif_count == 1:
                        motif_start = motif_indexes[keys][0][0]
                        motif_stop = motif_indexes[keys][0][1]
                        # generate motif object, draw motif
                        mymotif = Motif(motif_start, motif_stop, color)
                        mymotif.draw_motifs()
                        # draw motif color on legend
                        context.set_line_width(25)
                        context.set_source_rgba(color[0], color[1], color[2], color[3])
                        context.move_to(1115, y_value)        #(x,y)
                        context.line_to(1125, y_value)
                        context.stroke()
                        # add untranslated motif label to legend
                        context.set_source_rgba(0, 0, 0)
                        context.set_font_size(10)
                        context.select_font_face("Arial",
                                    cairo.FONT_SLANT_NORMAL,
                                    cairo.FONT_WEIGHT_NORMAL)
                        context.move_to(1130, y_value)
                        context.show_text(normal_motif)
                    # if there's multiple instances of the motif
                    elif motif_count > 1:
                        # iterate through the list of tuples in the motif dictionary values
                        for i in range(motif_count):
                            # generate motif objects, draw the multiple motifs
                            mymotif2 = Motif(motif_indexes[keys][i][0], motif_indexes[keys][i][1], color)
                            mymotif2.draw_motifs()
                            # draw motif color on legend
                            context.set_line_width(25)
                            context.set_source_rgba(color[0], color[1], color[2], color[3])
                            context.move_to(1115, y_value)        #(x,y)
                            context.line_to(1125, y_value)
                            context.stroke()
                            # add untranslated motif label to legend
                            context.set_source_rgba(0, 0, 0)
                            context.set_font_size(10)
                            context.select_font_face("Arial",
                                        cairo.FONT_SLANT_NORMAL,
                                        cairo.FONT_WEIGHT_NORMAL)
                            context.move_to(1130, y_value)
                            context.show_text(normal_motif)

# complete drawing
surface.write_to_png (png_name)
surface.finish()

# close files
fasta_one_line_file.close()
motifs.close()