# input_timeout

Define how long you want to wait for the user's input.
After the time is over, a default value is set. 

### Install it:

```python
pip install input-timeout
```

### Use it:

```python
from input_timeout import InputTimeout

        i = InputTimeout(
            timeout=20,
            input_message=" >> ",
            timeout_message="'Sorry, you were not fast enough'",
            defaultvalue="slow",
            cancelbutton="esc",
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=5,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough: ",
            defaultvalue="slow",
            cancelbutton="esc",
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="Wake up!",
            cancelbutton=None,
            show_special_characters_warning=None,
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >> ",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="Are you sleeping?",
            cancelbutton="esc",
            show_special_characters_warning=None,
        ).finalvalue
        print(f"\n\nYour input was {i}")

        i = InputTimeout(
            timeout=10,
            input_message=" >>",
            timeout_message="Sorry, you were not fast enough",
            defaultvalue="you are so slow",
            cancelbutton=None,
            show_special_characters_warning='If you want to use special characters, you have to use alt+\\d\\d\\d\\d\nPress "ctrl" to see a complete list of all combinations!',
        ).finalvalue
        print(f"\n\nYour input was {i}")
```

Output: 

```python
    #output
    If you want to use special characters, you have to use alt+\d\d\d\d
Press "ctrl" to see a complete list of all combinations!
 >>  babba
Your input was babba
If you want to use special characters, you have to use alt+\d\d\d\d
Press "ctrl" to see a complete list of all combinations!
alt+0192    ->    À        alt+0193    ->    Á        alt+0196    ->    Ä        alt+0194    ->    Â        
alt+0195    ->    Ã        alt+0197    ->    Å        alt+0198    ->    Æ        alt+0228    ->    ä        
alt+0224    ->    à        alt+0225    ->    á        alt+0226    ->    â        alt+0227    ->    ã        
alt+0229    ->    å        alt+0230    ->    æ        alt+0199    ->    Ç        alt+0231    ->    ç        
alt+0208    ->    Ð        alt+0240    ->    ð        alt+0203    ->    Ë        alt+0200    ->    È        
alt+0201    ->    É        alt+0202    ->    Ê        alt+0235    ->    ë        alt+0232    ->    è        
alt+0233    ->    é        alt+0234    ->    ê        alt+0207    ->    Ï        alt+0204    ->    Ì        
alt+0205    ->    Í        alt+0206    ->    Î        alt+0239    ->    ï        alt+0236    ->    ì        
alt+0237    ->    í        alt+0238    ->    î        alt+0209    ->    Ñ        alt+0241    ->    ñ        
alt+0214    ->    Ö        alt+0210    ->    Ò        alt+0211    ->    Ó        alt+0212    ->    Ô        
alt+0213    ->    Õ        alt+0216    ->    Ø        alt+0140    ->    Œ        alt+0246    ->    ö        
alt+0242    ->    ò        alt+0243    ->    ó        alt+0244    ->    ô        alt+0245    ->    õ        
alt+0248    ->    ø        alt+0156    ->    œ        alt+0138    ->    Š        alt+0223    ->    ß        
alt+0154    ->    š        alt+0222    ->    Þ        alt+0254    ->    þ        alt+0220    ->    Ü        
alt+0217    ->    Ù        alt+0218    ->    Ú        alt+0219    ->    Û        alt+0252    ->    ü        
alt+0249    ->    ù        alt+0250    ->    ú        alt+0251    ->    û        alt+0159    ->    Ÿ        
alt+0221    ->    Ý        alt+0255    ->    ÿ        alt+0253    ->    ý        alt+0168    ->    ¨        
alt+0136    ->    ˆ        alt+0180    ->    ´        alt+0175    ->    ¯        alt+0184    ->    ¸        
alt+0192    ->    À        alt+0193    ->    Á        alt+0196    ->    Ä        alt+0194    ->    Â        
alt+0195    ->    Ã        alt+0197    ->    Å        alt+0198    ->    Æ        alt+0228    ->    ä        
alt+0224    ->    à        alt+0225    ->    á        alt+0226    ->    â        alt+0227    ->    ã        
alt+0229    ->    å        alt+0230    ->    æ        alt+0199    ->    Ç        alt+0231    ->    ç        
alt+0208    ->    Ð        alt+0240    ->    ð        alt+0203    ->    Ë        alt+0200    ->    È        
alt+0201    ->    É        alt+0202    ->    Ê        alt+0235    ->    ë        alt+0232    ->    è        
alt+0233    ->    é        alt+0234    ->    ê        alt+0207    ->    Ï        alt+0204    ->    Ì        
alt+0205    ->    Í        alt+0206    ->    Î        alt+0239    ->    ï        alt+0236    ->    ì        
alt+0237    ->    í        alt+0238    ->    î        alt+0209    ->    Ñ        alt+0241    ->    ñ        
alt+0214    ->    Ö        alt+0210    ->    Ò        alt+0211    ->    Ó        alt+0212    ->    Ô        
alt+0213    ->    Õ        alt+0216    ->    Ø        alt+0140    ->    Œ        alt+0246    ->    ö        
alt+0242    ->    ò        alt+0243    ->    ó        alt+0244    ->    ô        alt+0245    ->    õ        
alt+0248    ->    ø        alt+0156    ->    œ        alt+0138    ->    Š        alt+0223    ->    ß        
alt+0154    ->    š        alt+0222    ->    Þ        alt+0254    ->    þ        alt+0220    ->    Ü        
alt+0217    ->    Ù        alt+0218    ->    Ú        alt+0219    ->    Û        alt+0252    ->    ü        
alt+0249    ->    ù        alt+0250    ->    ú        alt+0251    ->    û        alt+0159    ->    Ÿ        
alt+0221    ->    Ý        alt+0255    ->    ÿ        alt+0253    ->    ý        alt+0168    ->    ¨        
alt+0136    ->    ˆ        alt+0180    ->    ´        alt+0175    ->    ¯        alt+0184    ->    ¸        
Sorry, you were not fast enough: 
Your input was slow
 >>  super
Your input was super
 >>  adasa
Your input was adasa
If you want to use special characters, you have to use alt+\d\d\d\d
Press "ctrl" to see a complete list of all combinations!
Sorry, you were not fast enough
Your input was you are so slow
```
