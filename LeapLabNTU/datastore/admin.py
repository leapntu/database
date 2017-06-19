from django.contrib import admin
from .models import Language, Mother, Father, Baby, LanguagesKnownByFatherInOrderOfFluency, LanguagesKnownByMotherInOrderOfFluency, \
LanguageProficiencyOfMothersInSpeaking, LanguageProficiencyOfMothersInUnderstanding, LanguageProficiencyOfMothersInWriting,\
LanguageProficiencyOfMothersInReading, LanguageProficiencyOfFathersInSpeaking, LanguageProficiencyOfFathersInUnderstanding,\
LanguageProficiencyOfFathersInWriting, LanguageProficiencyOfFathersInReading, Session, Study, Occupation, BabyLanguageProfile, \
LanguageSpokenToBabyByMother, LanguageSpokenToBabyByFather, LanguageSpokenToBabyBySiblings, LanguageSpokenToBabyByMaternalGrandparents, \
LanguageSpokenToBabyByPaternalGrandparents, LanguageSpokenToBabyByRelatives, LanguageSpokenToBabyByOtherCaregivers, LanguageSpokenToBabyInSchool
import nested_admin

admin.site.register(Language)
admin.site.register(Session)
admin.site.register(Study)
admin.site.register(Occupation)

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

admin.site.register(BabyLanguageProfile, BabyLanguageProfileAdmin)
admin.site.register(Father, FatherAdmin)
admin.site.register(Mother, MotherAdmin)
admin.site.register(Baby, BabyAdmin)