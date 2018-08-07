import os
from optparse import OptionParser
import pyBigWig
from collections import defaultdict,Counter
import operator

def Info(infoStr):
    print("[%s] %s" %(time.strftime('%H:%M:%S'), infoStr))

def prepare_optparser():
    usage = "usage: %prog ......"
    description = "Input a H3K27ac file, and identify trough regions"
    description = "Demo command: python "
    optparser = OptionParser(version="%prog v1.00", description=description, usage=usage, add_help_option=False)

    optparser.add_option("-h","--help",action="help",help="Show this help message and exit.")
    optparser.add_option("-f","--file",dest="H3K27ac_bigwig_file",type="string",
                         help="Name of H3K27ac bigwig file")
    optparser.add_option("-p","--peaks",dest="H3K27ac_peak_file",type="string",
                         help="Name of H3K27ac peaks file")
    optparser.add_option("-n","--number",dest="output_trough_number",type=int,
                         help="Number of output trough",default=5000)

    (options,args) = optparser.parse_args()
    return(options)

def local_extreme(input,choice):
    values=[list(i) for i in input]
    if choice=="min":
        values.sort(key=operator.itemgetter(2))
        return values[0]
    if choice=="max":
        values.sort(key=operator.itemgetter(2),reverse=True)
        return values[0]

class sgRNA():
    def __init__(self, options):
        self.H3K27ac_bigwig_file = options.H3K27ac_bigwig_file
        self.H3K27ac_peak_file = options.H3K27ac_peak_file
        self.output_trough_number = options.output_trough_number
        self.search_regions = []

    def read_peaks(self):
        file=open(self.H3K27ac_peak_file)
        for line in file:
            elements=line.strip().split("\t")
            for i in range(int((int(elements[2])+500-int(elements[1])-500)/300)):
                center=int(elements[1])-500+(i+1)*300
                self.search_regions.append([elements[0],int(center-300),int(center+300)])

    def trough_finding(self):
        output=open("%s_trough_regions.bed" %(self.H3K27ac_bigwig_file),'w')
        coordinage_record=set()
        output_record=defaultdict(list)
        bw=pyBigWig.open(self.H3K27ac_bigwig_file)

        for peak in self.search_regions:
            try:
                values=bw.intervals(peak[0],peak[1],peak[2])
                mix_start, mix_end, mix_val = local_extreme(values,"min")
                if mix_start==peak[1] or mix_end==peak[2]:
                    pass
                else:
                    left_max_val=bw.stats(peak[0],mix_start-300,mix_start)[0]
                    right_max_val=bw.stats(peak[0],mix_end,mix_end+300)[0]

                    right_ratio_score=float(left_max_val)/mix_val
                    left_ratio_score=float(right_max_val)/mix_val

                    if right_ratio_score>1.5 and left_ratio_score>1.5:
                        temp=(peak[0],str(mix_start-150),str(mix_end+150))
                        if temp not in coordinage_record:
                            coordinage_record.add(temp)
                            output_record[peak[0]].append([mix_start-150,mix_end+150])
            except:
                pass

        output_record_v2=[]
        for key,values in output_record.items():
            values.sort(key=operator.itemgetter(0))
            temp=[]
            for i in values:
                if temp==[]:
                    temp=i
                else:
                    if i[0]<temp[1]:
                        temp[1]=i[1]
                    else:
                        output_record_v2.append([key]+temp)
                        temp=i

        final_record=[]
        for peak in output_record_v2:
            values=bw.intervals(peak[0],peak[1],peak[2])
            mix_start, mix_end, mix_val = local_extreme(values,"min")

            left_max_val=bw.stats(peak[0],mix_start-300,mix_start)[0]
            right_max_val=bw.stats(peak[0],mix_end,mix_end+300)[0]

            diff_score=(right_max_val+left_max_val)-(mix_val)

            new_start=int((mix_start+mix_end)/2)-100
            new_end=int((mix_start+mix_end)/2)+100
            final_record.append([peak[0],new_start,new_end,diff_score])

        final_record.sort(key=operator.itemgetter(3),reverse=True)
        for i in final_record[:self.output_trough_number]:
            insert=i[:3]
            output.write("%s\n" %"\t".join([str(k) for k in insert]))

def main():
    opts=prepare_optparser()
    g = sgRNA(opts)
    g.read_peaks()
    g.trough_finding()

if __name__ == "__main__":
    main()
