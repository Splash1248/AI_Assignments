from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

def build_alarm_network():
    model = DiscreteBayesianNetwork([
        ('Burglary', 'Alarm'),
        ('Earthquake', 'Alarm'),
        ('Alarm', 'JohnCalls'),
        ('Alarm', 'MaryCalls')
    ])

    cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
    cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])

    cpd_alarm = TabularCPD(
        variable='Alarm', variable_card=2,
        values=[[0.999, 0.71, 0.06, 0.05],
                [0.001, 0.29, 0.94, 0.95]],
        evidence=['Burglary', 'Earthquake'],
        evidence_card=[2, 2]
    )

    cpd_john = TabularCPD(
        variable='JohnCalls', variable_card=2,
        values=[[0.95, 0.10],
                [0.05, 0.90]],
        evidence=['Alarm'], evidence_card=[2]
    )

    cpd_mary = TabularCPD(
        variable='MaryCalls', variable_card=2,
        values=[[0.99, 0.30],
                [0.01, 0.70]],
        evidence=['Alarm'], evidence_card=[2]
    )

    model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_john, cpd_mary)
    model.check_model()

    return model

def run_inference():
    model = build_alarm_network()
    infer = VariableElimination(model)

    print("--- BAYESIAN NETWORK INFERENCE: ALARM SCENARIO ---\n")

    print("Query 1: What is the probability of a Burglary if BOTH John and Mary call?")
    q1 = infer.query(variables=['Burglary'], evidence={'JohnCalls': 1, 'MaryCalls': 1})
    print(q1)

    print("\nQuery 2: What is the probability of the Alarm sounding if there IS an Earthquake, but NO Burglary?")
    q2 = infer.query(variables=['Alarm'], evidence={'Earthquake': 1, 'Burglary': 0})
    print(q2)

if __name__ == "__main__":
    run_inference()
