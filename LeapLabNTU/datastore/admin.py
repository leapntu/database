from django.contrib import admin
from .models import Language, Mother, Father, Baby, LanguagesKnownByFatherInOrderOfFluency, LanguagesKnownByMotherInOrderOfFluency, \
LanguageProficiencyOfMothersInSpeaking, LanguageProficiencyOfMothersInUnderstanding, LanguageProficiencyOfMothersInWriting,\
LanguageProficiencyOfMothersInReading, LanguageProficiencyOfFathersInSpeaking, LanguageProficiencyOfFathersInUnderstanding,\
LanguageProficiencyOfFathersInWriting, LanguageProficiencyOfFathersInReading, Session, Study, Occupation, BabyLanguageProfile, \
LanguageSpokenToBabyByMother, LanguageSpokenToBabyByFather, LanguageSpokenToBabyBySiblings, LanguageSpokenToBabyByMaternalGrandparents, \
LanguageSpokenToBabyByPaternalGrandparents, LanguageSpokenToBabyByRelatives, LanguageSpokenToBabyByOtherCaregivers, LanguageSpokenToBabyInSchool, \
Household, HouseholdMember
import nested_admin

admin.site.register(Language)
admin.site.register(Session)
admin.site.register(Study)
admin.site.register(Occupation)
admin.site.register(HouseholdMember)

class LanguagesKnownByFatherInOrderOfFluencyInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguagesKnownByFatherInOrderOfFluency

class LanguagesKnownByMotherInOrderOfFluencyInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguagesKnownByMotherInOrderOfFluency

class LanguageProficiencyOfMothersInSpeakingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInSpeaking

class LanguageProficiencyOfMothersInUnderstandingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInUnderstanding

class LanguageProficiencyOfMothersInWritingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInWriting

class LanguageProficiencyOfMothersInReadingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInReading

class LanguageProficiencyOfFathersInSpeakingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInSpeaking

class LanguageProficiencyOfFathersInUnderstandingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInUnderstanding

class LanguageProficiencyOfFathersInWritingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInWriting

class LanguageProficiencyOfFathersInReadingInline(nested_admin.NestedStackedInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInReading

class FatherAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		LanguagesKnownByFatherInOrderOfFluencyInline,
		LanguageProficiencyOfFathersInSpeakingInline,
		LanguageProficiencyOfFathersInUnderstandingInline,
		LanguageProficiencyOfFathersInWritingInline,
		LanguageProficiencyOfFathersInReadingInline,
	]

class MotherAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		LanguagesKnownByMotherInOrderOfFluencyInline,
		LanguageProficiencyOfMothersInSpeakingInline,
		LanguageProficiencyOfMothersInUnderstandingInline,
		LanguageProficiencyOfMothersInWritingInline,
		LanguageProficiencyOfMothersInReadingInline,
	]

class LanguageSpokenToBabyByMotherInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByMother
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyByFatherInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByFather
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyBySiblingsInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyBySiblings
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyByMaternalGrandparentsInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByMaternalGrandparents
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyByPaternalGrandparentsInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByPaternalGrandparents
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyByRelativesInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByRelatives
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyByOtherCaregiversInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyByOtherCaregivers
	def get_extra(self, request, obj, **kwargs):
		return 0

class LanguageSpokenToBabyInSchoolInline(nested_admin.NestedStackedInline):
	model = LanguageSpokenToBabyInSchool
	def get_extra(self, request, obj, **kwargs):
		return 0

class BabyLanguageProfileInline(nested_admin.NestedStackedInline):
	model = BabyLanguageProfile
	inlines = [
		LanguageSpokenToBabyByMotherInline,
		LanguageSpokenToBabyByFatherInline,
		LanguageSpokenToBabyBySiblingsInline,
		LanguageSpokenToBabyByMaternalGrandparentsInline,
		LanguageSpokenToBabyByPaternalGrandparentsInline,
		LanguageSpokenToBabyByRelativesInline,
		LanguageSpokenToBabyByOtherCaregiversInline,
		LanguageSpokenToBabyInSchoolInline,
	]
	def get_extra(self, request, obj, **kwargs):
		return 0
	readonly_fields = ('last_modified', 'created_at', )

class BabyAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		BabyLanguageProfileInline,
	]
	readonly_fields = ('slug', )

class BabyLanguageProfileAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		LanguageSpokenToBabyByMotherInline,
		LanguageSpokenToBabyByFatherInline,
		LanguageSpokenToBabyBySiblingsInline,
		LanguageSpokenToBabyByMaternalGrandparentsInline,
		LanguageSpokenToBabyByPaternalGrandparentsInline,
		LanguageSpokenToBabyByRelativesInline,
		LanguageSpokenToBabyByOtherCaregiversInline,
		LanguageSpokenToBabyInSchoolInline,
	]
	readonly_fields = ('last_modified', 'created_at', )

class BabyInline(nested_admin.NestedStackedInline):
	model = Baby
	inlines = [
		BabyLanguageProfileInline,
	]
	def get_extra(self, request, obj, **kwargs):
		return 0

class FatherInline(nested_admin.NestedStackedInline):
	model = Father
	def get_extra(self, request, obj, **kwargs):
		return 0
	inlines = [
		LanguagesKnownByFatherInOrderOfFluencyInline,
		LanguageProficiencyOfFathersInSpeakingInline,
		LanguageProficiencyOfFathersInUnderstandingInline,
		LanguageProficiencyOfFathersInWritingInline,
		LanguageProficiencyOfFathersInReadingInline,
	]

class MotherInline(nested_admin.NestedStackedInline):
	model = Mother
	def get_extra(self, request, obj, **kwargs):
		return 0
	inlines = [
		LanguagesKnownByMotherInOrderOfFluencyInline,
		LanguageProficiencyOfMothersInSpeakingInline,
		LanguageProficiencyOfMothersInUnderstandingInline,
		LanguageProficiencyOfMothersInWritingInline,
		LanguageProficiencyOfMothersInReadingInline,
	]

class HouseholdMemberInline(nested_admin.NestedStackedInline):
	model = HouseholdMember
	def get_extra(self, request, obj, **kwargs):
		return 0

class HouseholdAdmin(nested_admin.NestedModelAdmin):
	inlines = [
		BabyInline,
		FatherInline,
		MotherInline,
		HouseholdMemberInline,
	]

admin.site.register(BabyLanguageProfile, BabyLanguageProfileAdmin)
admin.site.register(Father, FatherAdmin)
admin.site.register(Mother, MotherAdmin)
admin.site.register(Baby, BabyAdmin)
admin.site.register(Household, HouseholdAdmin)