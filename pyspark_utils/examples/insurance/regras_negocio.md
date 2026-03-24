##  🧩 Categorias de Regras de Negócio (Business Rules)
Estas regras são independentes de temporalidade ou consistência entre tabelas — são validações funcionais que garantem que os dados fazem sentido no contexto do negócio.

### APÓLICES
🔸prémio > 0  
🔸status permitido  
🔸tipo de produto válido  
🔸idade mínima do segurado  
🔸valor de franquia coerente (>= 0)  
🔸canal de venda permitido  

### DESCONTOS
🔸percentagem entre 0 e 100  
🔸desconto aplicável ao produto  
🔸valor monetário de desconto não pode exceder prémio  

### COBERTURAS
🔸cobertura compatível com o produto  
🔸valor segurado > 0  
🔸tipo de cobertura permitido  

### PSEGURAS
🔸idade mínima  
🔸tipo de pessoa válido (F/J)  
🔸género válido (M/F/Outro)  
🔸NIF válido (se aplicável)
  
### SINISTROS
🔸valor do sinistro > 0  
🔸tipo de sinistro permitido  
🔸sinistro não pode ser maior que valor segurado (regra comum)  


```
from pyspark.sql import functions as F

# ============================
# APÓLICES
# ============================

def check_positive_premium(df):
    """
    Regras de negócio: prémio deve ser > 0.
    """
    return df.filter(F.col("premium_amount") <= 0)


def check_valid_policy_status(df, allowed_status=None):
    """
    Regras de negócio: status da apólice deve estar na lista permitida.
    """
    if allowed_status is None:
        allowed_status = ["ATIVA", "CANCELADA", "SUSPENSA"]
    return df.filter(~F.col("policy_status").isin(allowed_status))


def check_valid_product_type(df, allowed_products=None):
    """
    Regras de negócio: tipo de produto deve ser válido.
    """
    if allowed_products is None:
        allowed_products = ["AUTO", "VIDA", "SAUDE", "HABITACAO"]
    return df.filter(~F.col("product_type").isin(allowed_products))


def check_minimum_age(df, min_age=18):
    """
    Regras de negócio: idade mínima do segurado.
    """
    return df.filter(F.col("customer_age") < min_age)


def check_valid_deductible(df):
    """
    Regras de negócio: franquia deve ser >= 0.
    """
    return df.filter(F.col("deductible") < 0)


# ============================
# DESCONTOS
# ============================

def check_discount_percentage(df):
    """
    Regras de negócio: percentagem de desconto deve estar entre 0 e 100.
    """
    return df.filter((F.col("discount_pct") < 0) | (F.col("discount_pct") > 100))


def check_discount_not_exceed_premium(df):
    """
    Regras de negócio: valor do desconto não pode exceder o prémio.
    """
    return df.filter(F.col("discount_amount") > F.col("premium_amount"))


# ============================
# COBERTURAS
# ============================

def check_valid_coverage_type(df, allowed_types=None):
    """
    Regras de negócio: tipo de cobertura deve ser permitido.
    """
    if allowed_types is None:
        allowed_types = ["ROUBO", "INCENDIO", "COLISAO", "VIDA"]
    return df.filter(~F.col("coverage_type").isin(allowed_types))


def check_positive_coverage_amount(df):
    """
    Regras de negócio: valor segurado deve ser > 0.
    """
    return df.filter(F.col("coverage_amount") <= 0)


# ============================
# PSEGURAS
# ============================

def check_valid_person_type(df):
    """
    Regras de negócio: tipo de pessoa deve ser F (física) ou J (jurídica).
    """
    return df.filter(~F.col("person_type").isin(["F", "J"]))


def check_valid_gender(df):
    """
    Regras de negócio: género deve ser válido.
    """
    return df.filter(~F.col("gender").isin(["M", "F", "OUTRO"]))


# ============================
# SINISTROS
# ============================

def check_positive_claim_amount(df):
    """
    Regras de negócio: valor do sinistro deve ser > 0.
    """
    return df.filter(F.col("claim_amount") <= 0)


def check_claim_not_exceed_coverage(df):
    """
    Regras de negócio: sinistro não pode exceder valor segurado.
    """
    return df.filter(F.col("claim_amount") > F.col("coverage_amount"))


```