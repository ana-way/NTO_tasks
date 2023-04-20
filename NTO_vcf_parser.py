def formating(vcf_str: str):
    if vcf_str.startswith('#'):
        return False
    else:
        vcf_l = vcf_str.split('\t')
        chr = vcf_l[0]
        position = vcf_l[1]
        ref_nucl = vcf_l[3]
        alt_nucl = vcf_l[4]
        res = f"chr{chr}:{position} {ref_nucl}/{alt_nucl}"
        return res

print(formating('5	112151205	-	G	.'))