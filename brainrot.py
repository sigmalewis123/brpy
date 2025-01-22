class Brainrott:
    def yap(self, stuff):
        print(stuff)

    def fanumtax(self, x, y):
        return x - y

    def skibidi(self, x, y):
        return x + y

    def mew(self, x):
        import time
        time.sleep(x)

    def looksmaxx(self, x):
        return input(x)

    def w(self):
        return True

    def l(self):
        return False


brainrot = Brainrott()

brainrot.yap(brainrot.fanumtax(9, 7))
brainrot.mew(3)
aura = brainrot.looksmaxx("Aura: ")

if int(aura) >= 10:
    aura = brainrot.w()
else:
    aura = brainrot.l()

while aura:
    brainrot.yap("+ aura")
    brainrot.mew(1)
