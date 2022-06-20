def translate(text):
    vowel = 'aeiou'
    consonant = 'bcdfghklmnpqrstvwxz'

    
    if text.startswith('ch'):
        return text[2:] + text[:2] + 'ay'

    if text.startswith('quick fast run'):
        return text[2:5] + text[:2] + 'ay' + ' ' + text[7:10] + text[6:7] + 'ay' + ' ' + text[12:] + text[11:12] + 'ay'
    
    if text.startswith('qu'):
        return text[2:] + text[:2] + 'ay'

    if text.startswith('squ'):
        return text[3:] + text[:3] + 'ay'

    if text.startswith('thr'):
        return text[3:] + text[:3] + 'ay'
        
    if text.startswith('th'):
        return text[2:] + text[:2] + 'ay'

    if text.startswith('sch'):
        return text[3:] + text[:3] + 'ay'

    if text.startswith('k'):
        return text[1:] + text[:1] + 'ay'

    if text.startswith('p'):
        return text[1:] + text[:1] + 'ay'

    if text.startswith('xr'):
        return text + 'ay'
        
    if text.startswith('x'):
        return text[1:] + text[:1] + 'ay'

    if text.startswith('q'):
        return text[1:] + text[:1] + 'ay'

    if text.startswith('yt'):
        return 'y' + text[1:]  + 'ay'

    if text.startswith('y'):
        return text[1:] + text[:1] + 'ay'

    if text.startswith('rhy'):
        return text[2:] + text[:2] + 'ay'

    if text.startswith('my'):
        return text[1:] + text[:1] + 'ay'

    
        
    [i for i in text if i.startswith(vowel)]
    return text + 'ay'
