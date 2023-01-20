import frappe
from frappe import _
from frappe.model.document import Document
from frappe.recorder import status

class JobOrder(Document):
    ## jobopening count decrementation
	def on_update(self):
		# get company name and required employee in joborder
		employee = frappe.get_all ('JobOrder', filters ={'sts':'Completed'},fields=['com','required_employee'])
		print(employee)
		# get company name and and job count in joborder
		company = frappe.get_all('company_listing',fields=['c_name','j_count'])
		print(company)
		# check if company name are same and upadte the job count based on completed job orders
		for i in range(len(employee)):
			for j in range(len(company)):
				if (employee[i]['com'] == company[j]['c_name']) and int(company[j]['j_count']) >= int(employee[i]['required_employee']):
					company_list= frappe.get_doc('company_listing',company[j]['c_name'])
					company_list.update({
						'j_count':int(company[j]['j_count'])-int(employee[i]['required_employee'])
					})
					company_list.save()

				elif  int(company[j]['j_count']) < int(employee[i]['required_employee']):
					frappe.msgprint("invalid required employee")

		# once the job count is updated then job will closed
		doc = frappe.get_all ('JobOrder', filters ={'sts':'Completed'},fields=['name'])
		for i in range(len(doc)):
			job_order=frappe.get_doc('JobOrder',doc[i]['name'])
			job_order.update({
				'sts':'Closed'
			})
			job_order.save()
		self.recommended_candidates()

	##recommendations
	def recommended_candidates(self):
		expected_skill_set=[]  #Stores expected skill set for the Job Order
		recommended_candidate_list=[]  #Stores candidate id of recommended Candidates

		candidate = frappe.get_all('Candidate list',pluck='name') #get all the candidate id from Candidate List

		#Get all current document if it is an active Job and get its skill set and add to expected skill set
	
		if self.sts == 'Active':
			for row in self.get("skill_set"):
				expected_skill_set.append(row.skill)
			print(expected_skill_set)

		#Iterate through the candidate skills if more than 2 skills matches get their Candidate Id
			
		for i in candidate:
			count=0
			candidate_skill = frappe.get_all('Expected Skill Set',filters={'parent':i}, pluck='skill')
			print(candidate_skill)
			for j in range(len(candidate_skill)):
				if candidate_skill[j] in expected_skill_set:
					count=count+1
			if(count>=2):
				recommended_candidate_list.append(i)

		final_recommended_candidates=list(set(recommended_candidate_list))
		
		#Now,iterate thorugh Candidate Id list and fetch their required details to add to recommended candidates (child table in Job Order)

		for i in range(len(final_recommended_candidates)):
			results=frappe.get_all("Candidate list",fields=["name as c_id","first_name","email_id","phone_number"],filters={"name":final_recommended_candidates[i]})
		#Append only the records not in the child table
			exists = False
			for can in self.candidates:
				if can.c_id == results[0]['c_id']:
					exists = True
					break
			if not exists:
				print(results[0])
				self.append("candidates",results[0])
		
		

					
		
				
		


    