

from math import *

# FROM MCCONNELL AND MA ##########################
# for complete answer it is 10^(ans) - in exp form for easier check - given equations in log_10
#found on page 2 under graph - over the radii rinf < r < reff
def MM13AllSigma(sigma):
    if (sigma == 200):
        ans = 8.32
    else:
        ans = (8.32 + (5.64 * log10(sigma / 200)))
    print(ans)

#found on page 9 on right side - over the radii rinf < r < reff
def MM13AllSigmaQuad(sigma):
    if (sigma == 200):
        ans = 8.28
    else:
        ans = (8.28 + (5.76 * log10(sigma / 200)) + (1.68 * pow(log10(sigma / 200), 2)))
    print(ans)

#found on page 11 under graph - over the radii 0 < r < reff
def MM13AllSigma0(sigma):
    if (sigma == 200):
        ans = 8.29
    else:
        ans = (8.29 + (5.48 * log10(sigma / 200)))
    print(ans)

#found on page 2 under graph - over the radii rinf < r < reff
def MM13EarlySigma(sigma):
    if (sigma == 200):
        ans = 8.39
    else:
        ans = (8.39 + (5.20 * log10(sigma / 200)))
    print(ans)

#found on page 2 under graph - over the radii rinf < r < reff
def MM13LateSigma(sigma):
    if (sigma == 200):
        ans = 8.07
    else:
        ans = (8.07 + (5.06 * log10(sigma / 200)))
    print(ans)

# all early type, in V-band, found on page 3 under graph
# for complete answer it is 10^(ans) - in exp form for easier check
def MM13EarlyLumBulge(lum):
    if (lum == pow(10, 11)):
        ans = 9.23
    else:
        ans = (9.23 + (1.11 * log10(lum / (pow(10, 11)))))
    print("10 ^",  ans)

#all early type, in V-band, found on page 4 under graph
# for complete answer it is 10^(ans) - in exp form for easier check
def MM13EarlyMassBulge(mass):
    if (mass == pow(10, 11)):
        ans = 8.46
    else:
        ans = (8.46 + (1.05 * log10(mass / (pow(10, 11)))))
    print("10 ^",  ans)


#FROM KORMENDY AND HO ###################################

#found on page 57 - for classical bulges and ellipticals
def KH13MassBulge(mass):
    ans = 0.49 * pow((mass / pow(10, 11)), 1.16) * pow(10, 9)
    print(ans) 
    
#found on page 55- for classical bulges and ellipticals
def KH13Sigma(sigma):
    if (sigma == 200):
        ans = 0.309 * pow(10, 9)
    else:
        ans = 0.309 * pow((sigma / 200), 4.38) * pow(10, 9)
    print(ans)
#found on page 55- for classical bulges and ellipticals
def KH13LumBulge(lum):
    ans = 0.542 * pow((lum / pow(10, 11)), 1.21) * pow(10, 9)
    print(ans)    
