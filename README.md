<div align="center">
<h2><code>KingJayan/boid-sim</code></h2>
</div>

simple boid simulation made using pygame

- [X] initialization
- [X] separation
- [ ] alignment
- [ ] cohesion
- [ ] other doohickeys(obstacles, evolution, specie behaviors)

rn its pretty ahh in terms of time complexity


`config.ts` - main configuration files
`util.py` - some math utility
`main.py` - game loop, functions, everything

## quickstart

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