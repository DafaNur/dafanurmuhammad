n= raw_input("masukan nama\n:  ")
ut= input("masukan nilai uts\n:  ")
us= input("masukan nilai uas\n:  ")
t= input("masukan nilai tugas\n:  ")
print "\n"
print "nama           : ", n
print "nilai uts      : ", ut
print "nilai uas      : ", us
print "nilai tugas    : ", t
akhir = (ut+us+t)/3
print "nilai akhir : ", akhir
print "\n"
if akhir >=80:
    print "nilai huruf :A"
    print "keterangan :lulus"
elif akhir >=70 and akhir <79:
    print "nilai huruf :B"
    print "keterangan :lulus"
elif akhir >=50 and akhir <69:
    print "nilai huruf :C"
    print "keterangan :tidak lulus"
elif akhir >=40 and akhir <49:
    print "nilai huruf :d"
    print "keterangan :lulus"
elif akhir >=0 and  akhir <39:
    print "nilai huruf :E"
    print "keterangan :tidak lulus"
