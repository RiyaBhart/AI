from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Intelligence', 'Grade'),
    ('StudyHours', 'Grade'),
    ('Difficulty', 'Grade'),
    ('Grade', 'Pass')
])

cpd_intelligence = TabularCPD(variable='Intelligence', variable_card=2,
                               values=[[0.7], [0.3]],
                               state_names={'Intelligence': ['High', 'Low']})

cpd_studyhours = TabularCPD(variable='StudyHours', variable_card=2,
                            values=[[0.6], [0.4]],
                            state_names={'StudyHours': ['Sufficient', 'Insufficient']})

cpd_difficulty = TabularCPD(variable='Difficulty', variable_card=2,
                            values=[[0.4], [0.6]],
                            state_names={'Difficulty': ['Hard', 'Easy']})

cpd_grade = TabularCPD(variable='Grade', variable_card=3,
                       values=[
                           [0.8, 0.6, 0.6, 0.4, 0.5, 0.3, 0.3, 0.1],  
                           [0.15, 0.3, 0.3, 0.4, 0.3, 0.4, 0.4, 0.3], 
                           [0.05, 0.1, 0.1, 0.2, 0.2, 0.3, 0.3, 0.6]  
                       ],
                       evidence=['Intelligence', 'StudyHours', 'Difficulty'],
                       evidence_card=[2, 2, 2],
                       state_names={
                           'Grade': ['A', 'B', 'C'],
                           'Intelligence': ['High', 'Low'],
                           'StudyHours': ['Sufficient', 'Insufficient'],
                           'Difficulty': ['Hard', 'Easy']
                       })

cpd_pass = TabularCPD(variable='Pass', variable_card=2,
                      values=[
                          [0.95, 0.8, 0.5],  
                          [0.05, 0.2, 0.5]   
                      ],
                      evidence=['Grade'],
                      evidence_card=[3],
                      state_names={
                          'Pass': ['Yes', 'No'],
                          'Grade': ['A', 'B', 'C']
                      })

model.add_cpds(cpd_intelligence, cpd_studyhours, cpd_difficulty, cpd_grade, cpd_pass)

assert model.check_model()

infer = VariableElimination(model)

result1 = infer.query(
    variables=['Pass'],
    evidence={'StudyHours': 'Sufficient', 'Difficulty': 'Hard'},
    show_progress=False
)

result2 = infer.query(
    variables=['Intelligence'],
    evidence={'Pass': 'Yes'},
    show_progress=False
)

print("Probability of passing given StudyHours=Sufficient and Difficulty=Hard:")
print(result1)

print("\nProbability of having High Intelligence given that student passed:")
print(result2)
