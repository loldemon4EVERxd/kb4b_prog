# prace_v_hodinach
Tento README slouží jako ukázka (a návod) k využití gitu.

## 0. Před začátkem – založení účtu
1. Otevři [https://github.com](https://github.com).
2. Založ vlastní účet pomocí školního emailu.
   (pokud už účet máš, klidně pracuj ve svém)
   
## 1. Vytvoření vlastního repozitáře (fork)
Tento repozitář je nastavený jako *read-only*. Pro možnost úprav si budete muset vytvořit vlastní verzi repozitáře - tzv. *fork*.
1. Na stránce tohoto repozitáře klikni vpravo nahoře na tlačítko **Fork**.
2. Vytvoří se **kopie repozitáře** pod tvým účtem:
   https://github.com/*tvoje-jmeno*/prace_v_hodinach

## 2. Klonování forku do VS Code (první použití)
1. Otevři **VS Code**.
2. Otevři paletu příkazů (**Ctrl+Shift+P**).
3. Zadej **Git: Clone**.
4. Vlož **URL svého forku** (ne originálu).
5. Vyber složku na disku.
6. Otevři naklonovaný repozitář ve VS Code.

## 3. Nastavení jména a e-mailu v Gitu (první použití)
Otevři terminál ve VS Code (**Ctrl+;**) a zadej:
```bash
git config --global user.name "Tvé jméno"
git config --global user.email "tvuj@email.cz"
```
Jméno odpovídá názvu tvého účtu.

## 4. Pullnutí z gitu
Pomocí pullnutí stáhneš změny v repozitáři z gitu do počítače.
1. Otevři repozitář ve VS Code.
2. Otevři terminál (Ctrl+;).
3. Stáhni nové změny:
```bash
git pull origin main
```

### 5. Nastavení učitelského repa jako *upstream*
Tímto nastavení můžeš stahovat změny z učitelského repozitáře do svého repozitáře
1. Zadej příkaz:
```bash
  git remote add upstream https://github.com/kb4b-2025/prace_v_hodinach
```
2. Změny z učitelského repa lze stáhnout pomocí:
```bash
  git fetch upstream
  git pull --rebase upstream main
```

### 6. Nahrání změn na git
1. Po každé větší změně je vhodné vytvořit *commit*:
```bash
  git add .
  git commit -m "Krátký název změny (např. Přidal funkci na výpočet průměru)"
```
2. Na konci hodiny nahraj změny na git pomoccí *push*:
```bash
  git push origin main
```
3. Stav repozitáře lze zkontroloat pomocí:
```bash
  git status
```

## Shrnutí „rituál každé hodiny“
1. **Na začátku**
   - `git pull origin main` (pro změny z tvého forku, např. z jiného PC)
   -  Případně stažení změn učitelského repa:
   -   `git fetch upstream` + `git pull --rebase upstream main`
2. **Během práce**
   - `git add .`  
   - `git commit -m "Krátký popis změny"`  

3. **Na konci**
   - `git push origin main` (ujisti se, že je vše na GitHubu)  
   - `git status` (zkontroluj stav repozitáře)
