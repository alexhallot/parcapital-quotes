# PAR Capital — Brand Guide

> Identidade visual da PAR Capital SA. Arquivo mídia-neutro: define **tokens** (fonte única da verdade) e mostra como aplicá-los em web, apresentações (PPTX) e documentos (DOCX).
>
> **Para reutilizar em outro projeto:** copie este arquivo para o repo novo. Os tokens não dependem de stack — adapte só a seção de aplicação correspondente.

---

## 1. Tokens

### 1.1 Cores

#### Marca (primárias)

| Token | Hex | Uso |
|---|---|---|
| `navy` | `#0d1526` | Cor principal. Headlines, fundos escuros, "PAR" no logo dark, barras 1 e 2 do logo |
| `navy-hover` | `#1a2a4a` | Hover de botões/links navy, estados ativos |
| `navy-2` | `#131e36` | Variante tonal de navy para gradientes ou fundos secundários em documentos formais (opcional) |
| `gold` | `#b8953f` | Cor de acento. "Capital" no wordmark, barra 3 do logo, destaques, ícones |
| `gold-hover` | `#d4b35c` | Hover do dourado |

#### Texto

| Token | Hex | Uso |
|---|---|---|
| `text` | `#1a1a1a` | Corpo principal |
| `text-label` | `#555` | Labels de formulário |
| `text-muted` | `#666` | Subtítulos, descrições |
| `text-subtle` | `#888` | Texto secundário |
| `text-minimal` | `#999` | Texto de baixa prioridade |
| `text-faint` | `#aaa` | Disclaimers, microtipografia |

#### Superfícies

| Token | Hex | Uso |
|---|---|---|
| `white` | `#ffffff` | Fundo padrão |
| `off-white` | `#fafafa` | Cards, seções alternadas |
| `light` | `#f5f5f5` | Fundo claro em documentos (PPTX/DOCX) |
| `dark` | `#080e1a` | Footer, mais escuro que navy |

#### Bordas

| Token | Hex | Uso |
|---|---|---|
| `border` | `#eee` | Bordas sutis |
| `border-md` | `#ddd` | Bordas de inputs |
| `border-lg` | `#e0e0e0` | Bordas mais marcadas |
| `border-xl` | `#f0f0f0` | Separadores muito leves |

#### Estados (funcionais)

| Token | Hex | Uso |
|---|---|---|
| `green` | `#1a7a4c` | Positivo, ícones de check, valorização |
| `green-bg` | `#f0f7f4` | Fundo de badges/ícones verde |
| `green-border` | `#d4eede` | Borda de badges verde |
| `red` | `#cc4444` | Negativo, X em comparativos, queda |
| `whatsapp` | `#25d366` | Botão flutuante do WhatsApp (apenas) |

#### Logo claro (sobre fundo escuro)

| Token | Hex | Uso |
|---|---|---|
| `logo-light-bars` | `#8a9bae` | Barras 1 e 2 do logo quando em fundo escuro |

---

### 1.2 Tipografia

| Contexto | Família | Pesos disponíveis |
|---|---|---|
| **Web** (site, app, dashboards) | `DM Sans`, sans-serif | 300, 400, 500, 600, 700 |
| **Wordmark do logo** | `DM Sans` 700, letter-spacing 3 | — |
| **Documentos formais** (PPTX títulos, DOCX cabeçalhos) | `Georgia`, serif | Regular, Bold |
| **Documentos formais** (PPTX corpo, DOCX corpo) | `Calibri` ou `Arial`, sans-serif | Regular, Bold |

> A serifa (Georgia) só aparece em material institucional formal — propostas, relatórios, decks executivos. Web é sempre DM Sans.

#### Escala (web)

| Token | Valor | Uso típico |
|---|---|---|
| `f-xs` | `11px` | Disclaimers |
| `f-sm` | `12px` | Labels, captions |
| `f-md` | `13px` | Texto auxiliar |
| `f-base` | `14px` | Corpo |
| `f-lg` | `15px` | Botões, CTAs |
| `f-xl` | `16px` | Subtítulos |
| `f-2xl` | `20px` | Títulos de card |
| `f-3xl` | `32px` | Títulos de seção |
| `f-stat` | `clamp(28px, 2.5vw, 36px)` | Números de destaque |
| `f-hero` | `clamp(36px, 3.5vw, 52px)` | Headline principal |
| `f-sub` | `clamp(16px, 1.2vw, 19px)` | Sub-headline |

#### Letter-spacing

- **Logo wordmark:** `3` (em SVG units, ajustar para `0.3em` em CSS quando necessário)
- **Section labels (uppercase):** `1.5px`
- **Headlines:** `-0.5px` a `-1px` (tracking apertado)

---

### 1.3 Border radius

| Token | Valor | Uso |
|---|---|---|
| `r-sm` | `6px` | Pequenos chips |
| `r-md` | `8px` | Inputs, botões, cards |
| `r-lg` | `12px` | Containers maiores |
| `r-xl` | `16px` | Cards de formulário, modais |
| `r-pill` | `100px` | Badges, pills |

---

### 1.4 Tom de voz

- **Institucional mas acessível** — não usa jargão financeiro gratuitamente
- **Sofisticado sem arrogância** — confiança vem dos fatos (regulação, custódia, números), não da retórica
- **Transparente e direto** — frases curtas, sem floreio, sem promessas vagas de retorno
- **Sempre menciona regulação** quando o contexto pede (BCU, FINRA, SIPC)

**Evitar:** linguagem motivacional ("realize seus sonhos"), exclamações, percentuais de retorno futuro, comparações pessoais.

---

## 2. Logo e ativos

### 2.1 Anatomia

```
[barra 1] [barra 2] [barra 3]  PAR  Capital
  navy    navy 50%   gold     navy  gold
```

- **3 barras verticais** (proporção 4.5w × 24h em viewBox 220×28, rx 0.5)
- **"PAR"** em navy (ou branco em fundo escuro), DM Sans 700, letter-spacing 3
- **"Capital"** em gold, DM Sans 700, letter-spacing 3
- **Espaço entre símbolo e texto:** 28 units (~10% da largura do logo)

### 2.2 Variações

| Variação | Quando usar | Barras 1+2 | "PAR" | "Capital" |
|---|---|---|---|---|
| **Dark** (logo escuro / fundo claro) | Navbar de site, papelaria branca | `#0d1526` (1) + `#0d1526` @ 50% (2) | `#0d1526` | `#b8953f` |
| **Light** (logo claro / fundo escuro) | Footer, slides navy, fundos escuros | `#8a9bae` (1) + `#8a9bae` @ 50% (2) | `#ffffff` | `#b8953f` |
| **Favicon / ícone** | Só as 3 barras, sem wordmark | `#0d1526` + `#0d1526` @ 50% + `#b8953f` | — | — |

### 2.3 Arquivos

Os SVGs estão como arquivos no repo — copie esta pasta inteira pra outro projeto:

| Arquivo | Variação | Uso típico |
|---|---|---|
| [assets/logo/par-capital-logo-dark.svg](assets/logo/par-capital-logo-dark.svg) | Dark | Navbar, fundos claros |
| [assets/logo/par-capital-logo-light.svg](assets/logo/par-capital-logo-light.svg) | Light | Footer, fundos escuros (navy) |
| [favicon.svg](favicon.svg) | Só barras | Favicon do navegador (na raiz por convenção) |

**Como usar em HTML:**

```html
<!-- Dark (fundo claro) -->
<img src="assets/logo/par-capital-logo-dark.svg" alt="PAR Capital" width="280" height="36">

<!-- Light (fundo escuro) -->
<img src="assets/logo/par-capital-logo-light.svg" alt="PAR Capital" width="180" height="24">

<!-- Favicon (no <head>) -->
<link rel="icon" type="image/svg+xml" href="favicon.svg">
```

> **⚠️ Atenção — fonte do wordmark:** quando o SVG é carregado via `<img>`, o navegador sandbox restringe acesso a fontes web. O texto "PAR Capital" cai pra fonte system-default (DM Sans não é renderizada). Como o wordmark é bold com letter-spacing alto, a diferença é sutil mas existe. Soluções:
> - **Aceitar fallback** (padrão atual) — funcional, look próximo o suficiente
> - **Converter texto em paths** com Inkscape/Figma (recomendado para produção crítica de marca)
> - **Embutir SVG inline** no HTML (preserva fonte mas perde a portabilidade do arquivo)

### 2.4 SVG inline — alternativa para projetos sem arquivos separados

Se não quiser copiar a pasta `assets/logo/`, cola o SVG direto no HTML:

**Versão dark (fundo claro):**

```html
<svg width="280" height="36" viewBox="0 0 220 28">
  <rect x="0"  y="2" width="4.5" height="24" rx="0.5" fill="#0d1526"/>
  <rect x="7"  y="2" width="4.5" height="24" rx="0.5" fill="#0d1526" opacity="0.5"/>
  <rect x="14" y="2" width="4.5" height="24" rx="0.5" fill="#b8953f"/>
  <text x="28" y="19" font-family="DM Sans,sans-serif" font-size="16" font-weight="700" letter-spacing="3" fill="#0d1526">PAR</text>
  <text x="76" y="19" font-family="DM Sans,sans-serif" font-size="16" font-weight="700" letter-spacing="3" fill="#b8953f">Capital</text>
</svg>
```

**Versão light (fundo escuro):**

```html
<svg width="180" height="24" viewBox="0 0 220 28">
  <rect x="0"  y="2" width="4.5" height="24" rx="0.5" fill="#8a9bae"/>
  <rect x="7"  y="2" width="4.5" height="24" rx="0.5" fill="#8a9bae" opacity="0.5"/>
  <rect x="14" y="2" width="4.5" height="24" rx="0.5" fill="#b8953f"/>
  <text x="28" y="19" font-family="DM Sans,sans-serif" font-size="16" font-weight="700" letter-spacing="3" fill="#ffffff">PAR</text>
  <text x="76" y="19" font-family="DM Sans,sans-serif" font-size="16" font-weight="700" letter-spacing="3" fill="#b8953f">Capital</text>
</svg>
```

**Favicon (só barras):**

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
  <rect x="3"  y="4" width="6" height="24" rx="1" fill="#0d1526"/>
  <rect x="13" y="4" width="6" height="24" rx="1" fill="#0d1526" opacity="0.5"/>
  <rect x="23" y="4" width="6" height="24" rx="1" fill="#b8953f"/>
</svg>
```

> Quando inline, a fonte DM Sans carregada pelo `<head>` da página renderiza corretamente no SVG — sem fallback.

### 2.5 Regras de uso

- **Tamanho mínimo:** 120px de largura (web) / 30mm (impresso). Abaixo disso, usar apenas o favicon (as 3 barras).
- **Clear space:** manter um espaço livre ao redor do logo igual à largura de **uma barra** (~4.5 units).
- **Nunca:** distorcer proporção, trocar cores das barras, usar o logo em fundos com baixo contraste, adicionar sombras/efeitos.
- **Fundo permitido:** branco, `off-white`, navy ou imagens com overlay escuro suficiente para preservar contraste do "PAR"/"Capital".

---

## 3. Aplicação por mídia

### 3.1 Web (CSS)

Copiar este bloco em `:root` no CSS principal:

```css
:root {
  /* Marca */
  --navy:       #0d1526;
  --navy-hover: #1a2a4a;
  --gold:       #b8953f;
  --gold-hover: #d4b35c;

  /* Texto */
  --text:         #1a1a1a;
  --text-muted:   #666;
  --text-subtle:  #888;
  --text-label:   #555;
  --text-faint:   #aaa;
  --text-minimal: #999;

  /* Superfícies */
  --white:     #fff;
  --off-white: #fafafa;
  --dark:      #080e1a;

  /* Bordas */
  --border:    #eee;
  --border-md: #ddd;
  --border-lg: #e0e0e0;
  --border-xl: #f0f0f0;

  /* Estados */
  --green:        #1a7a4c;
  --green-bg:     #f0f7f4;
  --green-border: #d4eede;
  --red:          #cc4444;
  --whatsapp:     #25d366;

  /* Tipografia */
  --font:    'DM Sans', sans-serif;
  --f-xs:    11px;
  --f-sm:    12px;
  --f-md:    13px;
  --f-base:  14px;
  --f-lg:    15px;
  --f-xl:    16px;
  --f-2xl:   20px;
  --f-3xl:   32px;
  --f-stat:  clamp(28px, 2.5vw, 36px);
  --f-hero:  clamp(36px, 3.5vw, 52px);
  --f-sub:   clamp(16px, 1.2vw, 19px);

  /* Raio */
  --r-sm:   6px;
  --r-md:   8px;
  --r-lg:   12px;
  --r-xl:   16px;
  --r-pill: 100px;
}
```

**Import da fonte (no `<head>`):**

```html
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
```

**Padrão de hover:**

```css
.btn-primary { background: var(--navy); }
.btn-primary:hover { background: var(--navy-hover); }
.link-gold { color: var(--gold); }
.link-gold:hover { color: var(--gold-hover); }
```

---

### 3.2 PPTX (apresentações)

**Slides:**
- **Alternância de fundo:** ímpar = navy `#0d1526` / par = branco `#ffffff`
- **Capa e closing:** sempre navy
- **Margem esquerda padrão:** 0.6"
- **Posições (em polegadas):**
  - Título: `x=0.6, y=0.3`
  - Subtítulo: `x=0.6, y=0.85`
  - Conteúdo: `y=1.35`
  - Footer: `y=5.25`

**Tipografia:**
- Títulos: **Georgia Bold** (serifada)
- Corpo: **Calibri** ou **Arial** Regular

**Elementos decorativos:**
- Barras verticais douradas a 30% e 15% de transparência (lembrar do logo)
- Linha horizontal gold sob títulos
- Ícones em círculos dourados sólidos
- Cards com `border-radius: 8px`

**Footer obrigatório:** `PAR Capital SA — Confidencial`

**Closing slide:** menção à regulação BCU (ver seção 4).

**Exemplo pptxgenjs — slide navy padrão:**

```js
const slide = pres.addSlide();
slide.background = { color: '0d1526' };
slide.addText('Título do slide', {
  x: 0.6, y: 0.3, w: 9, h: 0.5,
  fontFace: 'Georgia', fontSize: 28, bold: true,
  color: 'ffffff'
});
slide.addText('Subtítulo opcional', {
  x: 0.6, y: 0.85, w: 9, h: 0.4,
  fontFace: 'Calibri', fontSize: 14,
  color: 'b8953f'
});
// Linha gold decorativa
slide.addShape('line', {
  x: 0.6, y: 1.25, w: 1.5, h: 0,
  line: { color: 'b8953f', width: 2 }
});
slide.addText('PAR Capital SA — Confidencial', {
  x: 0.6, y: 5.25, w: 9, h: 0.3,
  fontFace: 'Calibri', fontSize: 9,
  color: '999999'
});
```

---

### 3.3 DOCX (relatórios e documentos)

- **Margens:** 2.5cm em todos os lados
- **Cabeçalhos:** Georgia Bold, cor `navy`
- **Corpo:** Calibri/Arial 11pt, cor `text` (`#1a1a1a`)
- **Linhas decorativas:** filete gold (`#b8953f`) de 1pt sob título principal
- **Logo:** versão dark no topo da primeira página (alinhado à esquerda, ~3cm de largura)
- **Footer:** `PAR Capital SA — Confidencial` + número da página, em cinza `#999`

---

## 4. Disclaimers e regulação

### 4.1 Português

> PAR Capital SA é uma gestora de ativos regulada pelo Banco Central do Uruguai (BCU). Os serviços de custódia e execução são prestados pela Interactive Brokers LLC, membro da FINRA e SIPC, que protege contas de clientes em até USD 500.000. Investimentos envolvem riscos. Rendimentos passados não garantem resultados futuros. Este site não constitui oferta de valores mobiliários em nenhuma jurisdição.

### 4.2 English

> PAR Capital SA is an asset management firm regulated by the Central Bank of Uruguay (BCU). Custody and execution services are provided by Interactive Brokers LLC, member of FINRA and SIPC, which protects client accounts up to USD 500,000. Investments involve risk. Past performance does not guarantee future results. This website does not constitute an offer of securities in any jurisdiction.

### 4.3 Español

> PAR Capital SA es una gestora de activos regulada por el Banco Central del Uruguay (BCU). Los servicios de custodia y ejecución son prestados por Interactive Brokers LLC, miembro de FINRA y SIPC, que protege cuentas de clientes hasta USD 500.000. Las inversiones implican riesgos. Rendimientos pasados no garantizan resultados futuros. Este sitio no constituye oferta de valores en ninguna jurisdicción.

### 4.4 Footer curto (PPTX/DOCX)

| Idioma | Texto |
|---|---|
| PT | `PAR Capital SA — Confidencial` |
| EN | `PAR Capital SA — Confidential` |
| ES | `PAR Capital SA — Confidencial` |

---

## 5. Posicionamento (referência rápida)

Pontos institucionais que toda peça de comunicação pode invocar:

- Gestão profissional **sem conflito de interesse** ("IB-first")
- Custódia na **Interactive Brokers**, não em custodiante próprio
- Proteção **SIPC até USD 500.000**
- **160+ mercados globais** (vs. "apenas EUA" dos concorrentes)
- Multi-moeda: **28 moedas** na mesma conta
- Regulação **BCU** (Banco Central do Uruguai)
- Público-alvo: investidores com **USD 50k+** na América Latina, Portugal e EUA

---

## 6. Contatos institucionais

| Canal | Valor |
|---|---|
| Email | `info@parcapitalwm.com` |
| WhatsApp | `+598 93 974 174` (`wa.me/59893974174`) |
| Site | `www.parcapitalwm.com` |
| Dashboard | `dashboard.parcapitalwm.com` |
