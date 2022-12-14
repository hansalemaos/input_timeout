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
alt+0192    ->    ??        alt+0193    ->    ??        alt+0196    ->    ??        alt+0194    ->    ??        
alt+0195    ->    ??        alt+0197    ->    ??        alt+0198    ->    ??        alt+0228    ->    ??        
alt+0224    ->    ??        alt+0225    ->    ??        alt+0226    ->    ??        alt+0227    ->    ??        
alt+0229    ->    ??        alt+0230    ->    ??        alt+0199    ->    ??        alt+0231    ->    ??        
alt+0208    ->    ??        alt+0240    ->    ??        alt+0203    ->    ??        alt+0200    ->    ??        
alt+0201    ->    ??        alt+0202    ->    ??        alt+0235    ->    ??        alt+0232    ->    ??        
alt+0233    ->    ??        alt+0234    ->    ??        alt+0207    ->    ??        alt+0204    ->    ??        
alt+0205    ->    ??        alt+0206    ->    ??        alt+0239    ->    ??        alt+0236    ->    ??        
alt+0237    ->    ??        alt+0238    ->    ??        alt+0209    ->    ??        alt+0241    ->    ??        
alt+0214    ->    ??        alt+0210    ->    ??        alt+0211    ->    ??        alt+0212    ->    ??        
alt+0213    ->    ??        alt+0216    ->    ??        alt+0140    ->    ??        alt+0246    ->    ??        
alt+0242    ->    ??        alt+0243    ->    ??        alt+0244    ->    ??        alt+0245    ->    ??        
alt+0248    ->    ??        alt+0156    ->    ??        alt+0138    ->    ??        alt+0223    ->    ??        
alt+0154    ->    ??        alt+0222    ->    ??        alt+0254    ->    ??        alt+0220    ->    ??        
alt+0217    ->    ??        alt+0218    ->    ??        alt+0219    ->    ??        alt+0252    ->    ??        
alt+0249    ->    ??        alt+0250    ->    ??        alt+0251    ->    ??        alt+0159    ->    ??        
alt+0221    ->    ??        alt+0255    ->    ??        alt+0253    ->    ??        alt+0168    ->    ??        
alt+0136    ->    ??        alt+0180    ->    ??        alt+0175    ->    ??        alt+0184    ->    ??        
alt+0192    ->    ??        alt+0193    ->    ??        alt+0196    ->    ??        alt+0194    ->    ??        
alt+0195    ->    ??        alt+0197    ->    ??        alt+0198    ->    ??        alt+0228    ->    ??        
alt+0224    ->    ??        alt+0225    ->    ??        alt+0226    ->    ??        alt+0227    ->    ??        
alt+0229    ->    ??        alt+0230    ->    ??        alt+0199    ->    ??        alt+0231    ->    ??        
alt+0208    ->    ??        alt+0240    ->    ??        alt+0203    ->    ??        alt+0200    ->    ??        
alt+0201    ->    ??        alt+0202    ->    ??        alt+0235    ->    ??        alt+0232    ->    ??        
alt+0233    ->    ??        alt+0234    ->    ??        alt+0207    ->    ??        alt+0204    ->    ??        
alt+0205    ->    ??        alt+0206    ->    ??        alt+0239    ->    ??        alt+0236    ->    ??        
alt+0237    ->    ??        alt+0238    ->    ??        alt+0209    ->    ??        alt+0241    ->    ??        
alt+0214    ->    ??        alt+0210    ->    ??        alt+0211    ->    ??        alt+0212    ->    ??        
alt+0213    ->    ??        alt+0216    ->    ??        alt+0140    ->    ??        alt+0246    ->    ??        
alt+0242    ->    ??        alt+0243    ->    ??        alt+0244    ->    ??        alt+0245    ->    ??        
alt+0248    ->    ??        alt+0156    ->    ??        alt+0138    ->    ??        alt+0223    ->    ??        
alt+0154    ->    ??        alt+0222    ->    ??        alt+0254    ->    ??        alt+0220    ->    ??        
alt+0217    ->    ??        alt+0218    ->    ??        alt+0219    ->    ??        alt+0252    ->    ??        
alt+0249    ->    ??        alt+0250    ->    ??        alt+0251    ->    ??        alt+0159    ->    ??        
alt+0221    ->    ??        alt+0255    ->    ??        alt+0253    ->    ??        alt+0168    ->    ??        
alt+0136    ->    ??        alt+0180    ->    ??        alt+0175    ->    ??        alt+0184    ->    ??        
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
