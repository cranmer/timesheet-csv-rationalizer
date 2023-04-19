import streamlit as st
import pandas as pd
from io import StringIO

st.write('# Time Tracking CSV rationalizer')
st.write('by Kyle Cranmer')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    #st.write(stringio)

    # To read file as string:
    #string_data = stringio.read()
    #st.write(string_data)

    output_filename = 'reformatted-'+uploaded_file.name
    inf = stringio
    #outf = open(output_filename,'w')
    header = inf.readline()
    new_header = ['Date','email','project code','activity','billable hours','non-billable hours','notes','\n']
    delimeter = ','
    outlines = [delimeter.join(new_header)]

    line_counter = 0
    for line_counter, line in enumerate(inf.readlines()):
        (date, email) = line.split(',')[0:2]
        proj_and_act_list = line.split(',')[2:]

        for item in proj_and_act_list:
            item = item[1:-1] #remove extra " at beginning and end 

            if len(item.split('|')) > 1:
                outlines.append(delimeter.join([date,email]+item.split('|'))+'\n')

    #outf.writelines(outlines)
    #st.write(outlines)

    st.write('**Success!** Reformatted {} rows into {} activities'.format(line_counter, len(outlines)))

    st.download_button(
        label="Download data as CSV",
        data=''.join(outlines),
        file_name=output_filename,
        mime='text/csv',
    )