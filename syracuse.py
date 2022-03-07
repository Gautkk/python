def Syracuse(u):
    if u%2==0:
        u=u//2
    else:
        u=3*u+1
    return u

def List_Syracuse_modif(u):
    L=[u]
    while u!=1:
        u=Syracuse(u)
        L.append(u)
    return L

print()
print("Conjecture de Syracuse")
print()
print("Saisie:")
u=int(input())
print()

print(List_Syracuse_modif(u))
