"""

¿ES UN ANAGRAMA?
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */

 """

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower(): ## Pasamos las pabaras a minúscula 
        return False                         ## para hacer la comparación y evitar si nos pasan una mayúscula
    return sorted(word_one.lower()) == sorted(word_two.lower()) # Usamos 'sorted' para ordenar las letras

print(is_anagram('Amor', 'Roma'))



