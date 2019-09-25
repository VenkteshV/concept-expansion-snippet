import paras
import shutil

def get_concepts():
    import modules.K as K
    if paras.parameter.language == 'en':
        import modules.prework_en as prework
        import modules.concept_sql_en as concept_sql
    if paras.parameter.language == 'zh':
        import modules.prework_zh as prework
        import modules.concept_sql_zh as concept_sql
    text = []
    with open(paras.path_list.input_seed, 'r', encoding='utf-8') as f:
        for line in f.read().split('\n'):
            if line != '':
                text.append(concept_sql.get_snippet(line))
    with open(paras.path_list.input, 'w', encoding='utf-8') as f:
        f.write('\n'.join(text))
    shutil.copy(paras.path_list.input_seed, paras.path_list.seed)
    prework.work()
    K.kp_extraction()

if __name__ == '__main__':
    get_concepts()