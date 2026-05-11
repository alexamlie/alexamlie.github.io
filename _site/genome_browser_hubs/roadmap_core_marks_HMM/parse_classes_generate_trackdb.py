import sys

if __name__=="__main__":
    if len(sys.argv)==4:
        class_file = sys.argv[1]
        cell_type_file = sys.argv[2]
        full_track_file = sys.argv[3]
        
        with open(class_file, 'r') as roadmap_classes, open(cell_type_file, 'wb') as cell_types, open(full_track_file, 'wb') as full_tracks:
            all_cells = []
            header_data = roadmap_classes.readline()
            header_idx =  {header_data[x]:x for x in range(len(header_data))}
            for line in roadmap_classes:
                line_data = line.strip().split("\t")
                cell_type_mnemonic = line_data[7]
                all_cells.append(cell_type_mnemonic)
                epigenome_name = line_data[8].replace("\312", " ")                

                ## write the track info
                full_tracks.write("    track HMM15_"+cell_type_mnemonic+'\n')
                full_tracks.write("    bigDataUrl "+line_data[0]+'_15_coreMarks_dense.bb\n')
                full_tracks.write("    parent RoadmapHMM15 off\n")
                full_tracks.write("    shortLabel "+cell_type_mnemonic+" ChromHMM\n")
                full_tracks.write("    longLabel "+epigenome_name+" Chromatin State Segmentation by HMM from Roadmap\n")
                full_tracks.write("    subGroups cellType="+cell_type_mnemonic+"\n")
                full_tracks.write("    type bigBed 9\n")
                full_tracks.write("    itemRgb On\n\n")

            ## when it's done, write out all the cell types
            cell_types.write(" ".join([x+"="+x for x in all_cells])+"\n")
