data = [11+12j,-35+0j,-3-21j,36-3j,23+0j,36-3j,-3-21j,-35+0j,11+12j,1-34j,-20-4j,-4+35j,-1+23j,-4+35j,-20-4j,1-34j];
length(data);
abs(conv(data, data))

a = [1+1j,2-1j,3+2j];
b = [1-1j,2+1j,3-2j]
abs(conv(a,b))
abs(conv(a,a))