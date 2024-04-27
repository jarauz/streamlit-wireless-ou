import streamlit as st
import numpy as np
import time


st.set_page_config(
    page_title="Wireless Digital Communications Calculator",
    page_icon="ect.ico",
    layout="wide",
    menu_items={
        'About': "App contents: Copyright Julio Aráuz, 2023"
    }
)

resultComputeOne = 1

def computeOne(a):
  resultComputeOne = a*2

st.image("ohio_logo_small.svg", width=200)
# SVG needed to be optimized svg from Inkscape save as to work
st.caption("McClure School - [Information and Telecommunication Systems Program](https://www.ohio.edu/mcclure)")
st.text("Digital communications & wireless systems calculator")


tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Power", "Path loss", "Free space propagation", "SNR", "Shannon", 'Units', 'C/I'])

with tab1:
  col1, col2 = st.columns(2)

  with col1:
    st.subheader('mW to dBm')
    n1 = st.number_input('Input power in [mW]', key='n1', format='%.4e')
    st.write('Power in [mW] = ', n1)
    # keys have to be different, but not necessarily match the
    # name of the returned variable e.g. n1 and n1
    pdBm = 10*np.log10(n1)
    output = "{:.4f}".format(pdBm)
    st.write('Power in [dBm] is = ', output, 'dBm')
    st.latex(r'''P_{dBm}=10 \times log_{10} \left( \frac{P_{mW}}{1mW}\right )''')

  with col2:
    st.subheader('dBm to mW')
    n2 = st.number_input('Input power in [dBm]', key='n2')
    st.write('Power in [dBm] = ', n2)
    pmW = np.power(10,n2/10)
    output = "{:.4e}".format(pmW)
    st.write('Power in [mW] is = ', output, 'mW')
    st.latex(r'''P_{mW}=10^{\left( \frac{P_{dBm}}{10} \right )}''')      


with tab2:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Free space path loss')
    st.caption('Type values of known parameters in the boxes.')
    n3 = st.number_input('Distance Tx to Rx in [Km]', key='n3')
    n4 = st.number_input('Frequency in [MHz]', key='n4')
    n5 = st.number_input('Path loss in [dB]', key='n5')
    st.latex(r'''PL_{dB}=20 \times log_{10}(d_{Km})+20 \times log_{10}(f_{MHz})+32.45''')      


  result1 = st.button(label="Compute path loss PL in [dB]")
  result2 = st.button(label="Compute distance d in [Km]")
  result3 = st.button(label="Compute frequency f in [MHz]")


  with col2:
    st.subheader('Model results')
    st.caption('Use the buttons to compute the unknown parameter and display the results.')
    if result1:
        pl = (20*np.log10(n3))+(20*np.log10(n4))+32.45
        output = "{:.4f}".format(pl)
        st.write('Distance Tx to Rx in [Km] is ', n3, 'Km')
        st.write('Frequency in [MHz] is ', n4, 'MHz')
        st.write('Path loss in [dB] is ', output, 'dB')
    if result2:
        d = np.power(10,((n5 - 32.45 - (20*np.log10(n4)))/20))
        output = "{:.4f}".format(d)
        st.write('Frequency in [MHz] is ', n4, 'MHz')
        st.write('Path loss in [dB] is ', n5, 'dB')
        st.write('Distance Tx to Rx in [Km] is ', output, 'Km')
        st.latex(r'''d_{Km} = 10^{\frac{PL_{dB} - 32.45 - 20 \times log_{10}(f_{MHz})}{20}}''')      
    if result3:
        f = np.power(10,((n5 - 32.45 - (20*np.log10(n3)))/20))
        output = "{:.4f}".format(f)
        st.write('Path loss in [dB] is ', n5, 'dB')
        st.write('Distance Tx to Rx in [Km] is ', n3, 'Km')
        st.write('Frequency in [MHz] is ', output, 'MHz')
        st.latex(r'''f_{MHz} = 10^{\frac{PL_{dB} - 32.45 - 20 \times log_{10}(d_{Km})}{20}}''')    


with tab3:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Free space propagation')
    st.caption('Type values of known parameters in the boxes.')
    n6 = st.number_input('Power received in [dBm] (Prx)', key='n6')
    n7 = st.number_input('Power transmitted in [dBm] (Ptx)', key='n7')
    n8 = st.number_input('Path Loss in [dB] (PL)', key='n8')
    n9 = st.number_input('Gain transmitting antenna [dB] (Gtx)', key='n9')
    n10 = st.number_input('Gain receiving antenna [dB] (Grx)', key='n10')
    st.latex(r'''Prx_{[dBm]}=Ptx_{[dBm]}-PL_{[dB]}+Gtx_{[dB]}+Grx_{[dB]}''')

    result4 = st.button(label="Compute Prx in [dBm]")
    result5 = st.button(label="Compute Ptx in [dBm]")
    result6 = st.button(label="Compute PL in [dB]")
    result7 = st.button(label="Compute Gtx in [dB]")
    result8 = st.button(label="Compute Grx in [dB]")

  with col2:
    st.subheader('Model results')
    st.caption('Use the buttons to compute the unknown parameter and display the results.')
    if result4:
      prx = n7-n8+n9+n10
      output = "{:.4f}".format(prx)
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Power received in [dBm] is ', output, '[dBm]')

    if result5:
      ptx = n6+n8-n9-n10
      output = "{:.4f}".format(ptx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Power transmitted in [dBm] is ', output, '[dBm]')
      st.latex(r'''Ptx_{[dBm]}=Prx_{[dBm]}+PL_{[dB]}-Gtx_{[dB]}-Grx_{[dB]}''')

    if result6:
      pl = n7-n6+n9+n10
      output = "{:.4f}".format(pl)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Path loss in [dB] is ', output, '[dB]')
      st.latex(r'''PL_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+Gtx_{[dB]}+Grx_{[dB]}''')

    if result7:
      gtx = n6-n7+n8-n10
      output = "{:.4f}".format(gtx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', n10, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', output, '[dB]')
      st.latex(r'''Gtx_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+PL_{[dB]}-Grx_{[dB]}''')

    if result8:
      grx = n6-n7+n8-n9
      output = "{:.4f}".format(grx)
      st.write('Power received in [dBm] is ', n6, '[dBm]')
      st.write('Power transmitted in [dBm] is ', n7, '[dBm]')
      st.write('Path loss in [dB] is ', n8, '[dB]')
      st.write('Gain transmitting antenna in [dB] is', n9, '[dB]')
      st.write('Gain of receiving antenna in [db] is ', output, '[dB]')
      st.latex(r'''Grx_{[dB]}=Ptx_{[dBm]}-Prx_{[dBm]}+PL_{[dB]}-Gtx_{[dB]}''')

with tab4:
  st.subheader("Signal to noise ratio (SNR) computations")
  col1, col2, col3 = st.columns(3, gap="large")
  with col1:
    st.caption('Enter signal and noise powers in mW to compute SNR in numerical format and dB.')
    n11 = st.number_input('Signal power in [mW] (Ps)', key='n11', format='%.10f')
    n12 = st.number_input('Noise power in [mW] (Pn)', key='n12', format='%.4e')
    st.write('Signal power in [mW] = ', n11)
    st.write('Noise power in [mW] = ', n12)
    snr_nf = np.divide(n11,n12)
    snr_db = 10 * np.log10(np.divide(n11,n12))
    output1 = "{:.4f}".format(snr_nf)
    output2 = "{:.4f}".format(snr_db)
    if n12==0:
      output1 = np.inf
      output2 = np.inf
    st.write('SNR (numerical) is ', output1)
    st.write('SNR in [dB] is', output2, 'dB')
    st.latex(r'''\text{SNR}=\frac{P_s}{P_n}''')
    st.latex(r'''\text{SNR}_{dB}=10 \times log_{10} \left( \frac{P_s}{P_n} \right )''')

  with col2:
    st.caption('Enter signal and noise powers in dBm to compute SNR in numerical format and dB.')
    n13 = st.number_input('Signal power in [dBm] (Ps)', key='n13', format='%.4f')
    n14 = st.number_input('Noise power in [dBm] (Pn)', key='n14', format='%.4e')
    st.write('Signal power in [dBm] = ', n13)
    st.write('Noise power in [dBm] = ', n14)
    snr_db = n13 - n14
    snr_nf = np.power(10,np.divide(snr_db,10))
    output1 = "{:.4f}".format(snr_nf)
    output2 = "{:.4f}".format(snr_db)
    st.write('SNR (numerical) is ', output1)
    st.write('SNR in [dB] is', output2, 'dB')
    st.latex(r'''\text{SNR}_{dB}=P_s [\text{dBm}] - P_n [\text{dBm}]''')

  with col3:
    st.caption('Enter SNR in numerical format or in dB. Compute SNR in both formats.')
    n15 = st.number_input('SNR numerical format (SNR)', key='n15', format='%.4f')
    n16 = st.number_input('SNR in [dB] (SNR)', key='n16', format='%.4f')
    result9 = st.button(label="Compute SNR in dB")
    result10 = st.button(label="Compute numerical SNR")

    if result9:
      snr_db = 10 * np.log10(n15)
      output1 = "{:.4f}".format(snr_db)
      st.write('For SNR ', n15, '(numerical format) ', ', SNR in [dB] is', output1, 'dB')
      st.latex(r'''\text{SNR}_{dB}=10 \times log_{10} (\text{SNR})''')
    if result10:
      snr_nf = np.power(10,n16/10)
      output2 = "{:.4f}".format(snr_nf)
      st.write('For SNR ', n16, '[dB] ', ', SNR (numerical) is ', output2)
      st.latex(r'''\text{SNR}=10^{\left ( \frac{\text{SNR}_{dB}}{10} \right )} ''')

with tab5:
  col1, col2 = st.columns(2)
  with col1:
    st.subheader('Shannon-Hartley Theorem')
    st.caption('Type values of known parameters in the boxes.')
    n17 = st.number_input('Bandwidth in [Hz] (B)', key='n17')
    n18 = st.number_input('Numerical SNR (SNR)', key='n18')
    n19 = st.number_input('Channel capacity in [bps] (C)', key='n19')
    st.latex(r'''C_{bps}=B_{Hz} \times log_{2}(1+\text{SNR})''')      


    result11 = st.button(label="Compute capacity C in [bps]")
    result12 = st.button(label="Compute bandwidth in [Hz]")
    result13 = st.button(label="Compute SNR numerical and SNR in dB")


  with col2:
    st.subheader('Model results')
    st.caption('Use the buttons to compute the unknown parameter and display the results.')
    if result11:
        c = n17*np.log2(1+n18)
        output = "{:.4f}".format(c)
        st.write('Bandwidth in [Hz] is ', n17, 'Hz')
        st.write('Numerical SNR is ', n18)
        st.write('Channel capacity in [bps] is ', output, 'bps')
    if result12:
        b = n19/np.log2(1+n18)
        output = "{:.4f}".format(b)
        st.write('Numerical SNR is ', n18)
        st.write('Channel capacity in [bps] is ', n19, 'bps')
        st.write('Bandwidth in [Hz] is ', output, 'Hz')
        st.latex(r'''B_{Hz}=\frac{C_{bps}}{log_{2}(1+\text{SNR})}''')      
    if result13:
        s = np.power(2,np.divide(n19,n17))-1
        output = "{:.4f}".format(s)
        st.write('Channel capacity in [bps] is ', n19, 'bps')
        st.write('Bandwidth in [Hz] is ', n17, 'Hz')
        st.write('Numerical SNR is ', output)
        st.write('SNR in [dB] is', 10*np.log10(s), 'dB')
        st.latex(r'''\text{SNR}=2^{\frac{C_{bps}}{B_{Hz}}}-1''')    

with tab6:
  st.subheader('Power')
  col11, col12, col13 = st.columns(3)
  with col11:
    n20 = st.number_input('Power in Watts (W)', key='n20')
    n21 = st.number_input('Power in mW (mW)', key='n21')
  with col12:
    st.write('Unit transformation:')
    result14 = st.button(label="Compute power in mW")
    result15 = st.button(label="Compute power in W")
  with col13:
    st.write('Results:')
    if result14:
      pmw = n20 * 1000
      output = "{:.4f}".format(pmw)
      st.write(n20, "W", " is equal to ", output, "mW")
    if result15:
      pw = n21 / 1000
      output = "{:.6f}".format(pw)
      st.write(n21, "mW", " is equal to ", output, "W")
      
  st.subheader('Frequency')
  col21, col22, col23 = st.columns(3)
  with col21:
    n22 = st.number_input('Frequency in [Hz] (f)', key='n22')
    n23 = st.number_input('Frequency in [MHz] (f)', key='n23')
  with col22:
    st.write('Unit transformation:')
    result16 = st.button(label="Compute frequency in [MHz]")
    result17 = st.button(label="Compute frequency in [Hz]")
  with col23:
    st.write('Results:')
    if result16:
      fmhz= n22 / 1000000
      output = "{:.4f}".format(fmhz)
      st.write(n22, "Hz", " is equal to ", output, "MHz")
    if result17:
      fhz = n23 * 1000000
      output = "{:.4f}".format(fhz)
      st.write(n23, "MHz", " is equal to ", output, "Hz")


with tab7:
  col71, col72 = st.columns(2)
  with col71:
    st.subheader('Reuse factor 1/K')
    n24 = st.number_input('Carrier / Interference (dB)', key='n24')
    n25 = st.number_input(r'Environmental exponent ${\alpha}$', key='n25')
    st.write('C is the power of the carrier')
    st.write('I is the total power of interferers')
    result18 = st.button(label="Compute reuse factor 1/K")
    if result18:
      if (n25 > 0):
        ciNum = np.power(10,n24/10)
        output = (np.power(6*ciNum,(2/n25)))/3
        st.write('C/I in [dB] is ', n24, 'dB')
        st.write(r"${\alpha}$ is ", n25)
        st.write('C/I numerical is ', format(ciNum, ".4f"))
        st.write('K value is ', format(output, ".4f"))
        st.write('Then K to be used is ', np.ceil(output))
        st.write('Reuse factor 1/K is ', '1/',np.ceil(output))
        st.latex(r'''K=\frac{1}{3}{\left( \frac{6C}{I} \right)}^{\frac{2}{\alpha}}''')
      else:
        st.write(r"${\alpha}$ should be greater than zero")
  with col72:
    st.subheader('Carrier/Interference (C/I)')
    n26 = st.number_input('K', key='n26')
    n27 = st.number_input(r'Environmental exponent ${\alpha}$', key='n27')
    st.write('K is the number of cells in a cluster')
    result19 = st.button(label="Compute Carrier/Interference (C/I)")
    if result19:
      if (n27 > 0):
        st.write('K value is ', n26)
        st.write(r"${\alpha}$ is ", n27)
        output = (np.power(3*n26, (n27/2)))/6
        st.write('C/I numerical is ', format(output, ".4f"))
        st.write('C/I in [dB] is ', format(10*np.log10(output), ".4f"))
        st.latex(r'''\frac{C}{I}=\frac{1}{6}{(3K)}^{\frac{\alpha}{2}}''')
      else:
        st.write(r"${\alpha}$ should be greater than zero")
    
    
