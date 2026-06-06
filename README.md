# Sistema Hospitalar

Esse projeto foi desenvolvido como atividade avaliativa da disciplina de Desenvolvimento de APIs com FastAPI.

O nicho escolhido foi um sistema hospitalar, onde criei duas entidades: Médico e Consulta. A relação entre elas se dá pelo campo medico_id dentro de Consulta, que indica qual médico está responsável por aquela consulta.

## Entidades

**Médico**
- id (int)
- nome (str)
- especialidade (str)
- ativo (bool)
- salario (float)

**Consulta**
- id (int)
- paciente_nome (str)
- medico_id (int)
- data (str)
- realizada (bool)
- valor (float)

Desenvolvido por Wiverson Kauã de Sousa Duarte
