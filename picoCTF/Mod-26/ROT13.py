# a ROT13 converter

invalue = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}"

a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
b = "abcdefghijklmnopqrstuvwxyz"

out = ""

for n in invalue:
    if n in a:
        out += a[(a.index(n)+13)%len(a)]
    elif n in b:
        out += b[(b.index(n)+13)%len(b)]
    else:
        out += n

print(out)
