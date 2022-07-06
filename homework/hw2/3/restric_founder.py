from Bio.Restriction import Analysis, AllEnzymes, RestrictionBatch
from Bio import SeqIO

mito_gene = SeqIO.parse('NC_012920.1_HumanMitoGenome.fasta', 'fasta')
nuclear_genome = SeqIO.parse('GRCh37_latest_genomic.fna', 'fasta')


for record in mito_gene:
    mito_ana = Analysis(AllEnzymes, record.seq)
    not_mito = RestrictionBatch(mito_ana.without_site())


good_res = set()
for record in nuclear_genome:
    nuclear_ana = Analysis(not_mito, record.seq)
    restrictions = nuclear_ana.with_sites()
    for enzyme, positions in restrictions.items():
        for pos in range(len(positions)):
            if positions[pos]-positions[pos-1] <= 15000:
                good_res.add(enzyme)

print(good_res)

# test result for 2 seq file:
# PmaCI, PauI, AasI, TspARh3I, PteI, NotI, Acc16I, MabI, BsePI, PspCI, SalI, Sse8387I, PspOMII, Eco72I, MteI, BshTI, AspJHL3II, SmiI, PsrI, SgsI, FspI, TspMI, SgrAII, DraIII, ArsI, RpaBI, AsiGI, RpaB5I, XmaI, FspAI, Bsp1407I, Bsp460III, SfiI, SstE37I, GauT27I, TssI, BbrPI, MspSC27II, FseI, Pst273I, BoxI, SmaI, BsaBI, CsiI, DrdI, McaTI, Bse8I, CspCI, BglII, DseDI, AscI, MstI, HspMHR1II, NpeUS61II, PmlI, Cfr9I, MreI, BssHII, AgeI, AcvI, UbaF12I, PshAI, UbaF13I, BstPAI, Ssp714II, PinAI, BseJI, Sse232I, NsbI, CciNI, BstAUI, AdeI, RigI, PfrJS12V, Sth20745III, BsrGI, SexAI, SbfI, BspGI, Ecl35734I, CspAI, CcrNAIII, SwaI, SdaI, PalAI}