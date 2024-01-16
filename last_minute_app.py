
from normalzombie import p1
from babyzombie import p2
from mamazombie import p3
from babyzombietroika import p5
from troikaweapon import p4
from mamazombietroika import p6
from babydullpencil import p8
from dullpencil import p7
from dullpencilmamazomb import p9
from babyzombiesharpened import p10
from normalzombiesharpened import p11
from mamazombiesharmpenedpencil import p12
from safetyscissors import p13
from safteyscissors2 import p14
from safteyscissors3 import p15
from openedpaperclip import p16
from openedpaperclip2 import p17
from openedpaperclip3 import p18
from heavypackpack import p19
from heavybackpack2 import p20
from heavybackpack3 import p21
import random
import time




xl=print("This is the weapon list: none, troika, dull pencil, sharpened pencil, safety scissors, opened paper clip, and a heavy backpack")
pl= input("What is your weapon?:").strip().title()


if pl== "NONE":
    p2
    p1
    p3
elif pl=="TROIKA":
    p5
    p4
    p6
elif pl=="DULLPENCIL":
    p8
    p7
    p9
elif pl== "SHARPENEDPENCIL":
    p11
    p10
    p12
elif pl=="SAFETYSCISSORS":
    p14
    p13
    p15
elif pl=="OPENEDPAPERCLIP":
    p17
    p16
    p18
elif pl=="HEAVYBACKPACK":
    p20
    p19
    p21
else: 
    print("Invalid") 
