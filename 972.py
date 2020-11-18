#972. Equal Rational Numbers

class Solution:
    def isRationalEqual(self, S: str, T: str) -> bool:
        try:
            S_integer, S_rational = S.split('.')
        except:
            S_integer = S
            S_rational = ''
        try:
            T_integer, T_rational = T.split('.')
        except:
            T_integer = T
            T_rational = ''
        if '(' in S_rational:
            S_NonRepeating, S_Repeating = S_rational.split('(')
            S_Repeating = S_Repeating[:-1]
            if S_NonRepeating:
                S_final = int(S_integer) + (int(S_NonRepeating + S_Repeating) - int(S_NonRepeating))/int((len(S_Repeating) * '9') + len(S_NonRepeating) * '0')
            else:
                S_final = int(S_integer) + int(S_Repeating)/int(len(S_Repeating) * '9')
        else:
            S_final = float(S_integer + '.' + S_rational)
        if '(' in T_rational:
            T_NonRepeating, T_Repeating = T_rational.split('(')
            T_Repeating = T_Repeating[:-1]
            if T_NonRepeating:
                T_final = int(T_integer) + (int(T_NonRepeating + T_Repeating) - int(T_NonRepeating))/int((len(T_Repeating) * '9') + len(T_NonRepeating) * '0')
            else:
                T_final = int(T_integer) + int(T_Repeating)/int(len(T_Repeating) * '9')
        else:
            T_final = float(T_integer + '.' + T_rational)
        if S_final == T_final:
            return True
        else:
            return False
