from django.contrib import admin
from .models import Language, Mother, Father, Baby, LanguagesKnownByFatherInOrderOfFluency, LanguagesKnownByMotherInOrderOfFluency, \
LanguageProficiencyOfMothersInSpeaking, LanguageProficiencyOfMothersInUnderstanding, LanguageProficiencyOfMothersInWriting,\
LanguageProficiencyOfMothersInReading, LanguageProficiencyOfFathersInSpeaking, LanguageProficiencyOfFathersInUnderstanding,\
LanguageProficiencyOfFathersInWriting, LanguageProficiencyOfFathersInReading, LanguageSpokenToBabyByMother,\
LanguageSpokenToBabyByFather, LanguageSpokenToBabyBySiblings, LanguageSpokenToBabyByMaternalGrandparents,\
LanguageSpokenToBabyByPaternalGrandparents, LanguageSpokenToBabyByRelatives, LanguageSpokenToBabyByOtherCaregivers,\
LanguageSpokenToBabyInSchool, Session, Study

admin.site.register(Language)
admin.site.register(Session)
admin.site.register(Study)

class LanguagesKnownByFatherInOrderOfFluencyInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguagesKnownByFatherInOrderOfFluency

class LanguagesKnownByMotherInOrderOfFluencyInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguagesKnownByMotherInOrderOfFluency

class LanguageProficiencyOfMothersInSpeakingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInSpeaking

class LanguageProficiencyOfMothersInUnderstandingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInUnderstanding

class LanguageProficiencyOfMothersInWritingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInWriting

class LanguageProficiencyOfMothersInReadingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfMothersInReading

class LanguageProficiencyOfFathersInSpeakingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInSpeaking

class LanguageProficiencyOfFathersInUnderstandingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInUnderstanding

class LanguageProficiencyOfFathersInWritingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInWriting

class LanguageProficiencyOfFathersInReadingInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageProficiencyOfFathersInReading

class FatherAdmin(admin.ModelAdmin):
	inlines = [
		LanguagesKnownByFatherInOrderOfFluencyInline,
		LanguageProficiencyOfFathersInSpeakingInline,
		LanguageProficiencyOfFathersInUnderstandingInline,
		LanguageProficiencyOfFathersInWritingInline,
		LanguageProficiencyOfFathersInReadingInline,
	]

class MotherAdmin(admin.ModelAdmin):
	inlines = [
		LanguagesKnownByMotherInOrderOfFluencyInline,
		LanguageProficiencyOfMothersInSpeakingInline,
		LanguageProficiencyOfMothersInUnderstandingInline,
		LanguageProficiencyOfMothersInWritingInline,
		LanguageProficiencyOfMothersInReadingInline,
	]

class LanguageSpokenToBabyByMotherInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByMother

class LanguageSpokenToBabyByFatherInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByFather

class LanguageSpokenToBabyBySiblingsInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyBySiblings

class LanguageSpokenToBabyByMaternalGrandparentsInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByMaternalGrandparents

class LanguageSpokenToBabyByPaternalGrandparentsInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByPaternalGrandparents

class LanguageSpokenToBabyByRelativesInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByRelatives

class LanguageSpokenToBabyByOtherCaregiversInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyByOtherCaregivers

class LanguageSpokenToBabyInSchoolInline(admin.TabularInline):
	def get_extra(self, request, obj, **kwargs):
		return 0
	model = LanguageSpokenToBabyInSchool

class BabyAdmin(admin.ModelAdmin):
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

admin.site.register(Father, FatherAdmin)
admin.site.register(Mother, MotherAdmin)
admin.site.register(Baby, BabyAdmin)