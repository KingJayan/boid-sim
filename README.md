<div align="center">
<h2><code>KingJayan/boid-sim</code></h2>
<p>simple boid simulation made using pygame</p>
</div>

## todo
- [X] initialization
- [X] separation
- [ ] alignment
- [ ] cohesion
- [ ] other doohickeys(obstacles, evolution, specie behaviors)

## notes
- rn its pretty ahh in terms of time complexity
    - O(n^2) neighbor checks per frame, **will optimize later**


`config.py` - main configuration files

`util.py` - math utility

`main.py` - game loop, functions, everything

## quickstart

### prereqs
`python` -- 3.10+

### clone the repo
```bash
git clone https://github.com/KingJayan/boid-sim
```

### uv venv setup (optional)
```bash
pip install uv
uv python install 3.12
uv pip install -r requirements.txt
```

### run it
```bash
python main.py
```