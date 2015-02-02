#### 0.5.0 ####
 * Support Django 1.6.
 * Add virtual `translation` and `translation_LANGUAGE_CODE` fields. The fields are descriptors returning translation
   instances.

#### 0.4.0 ####
 * Support Django 1.4 and 1.5.
 * Upgrade flatpages.
 * Change in flatpages database structure (PostgreSQL):

   ```sql
   ALTER TABLE "multilingual_flatpage_sites" RENAME COLUMN "multilingualflatpage_id" TO "flatpage_id";
   ```

    OR (MySQL):

   ```sql
   ALTER TABLE `multilingual_flatpage_sites` CHANGE `multilingualflatpage_id` `flatpage_id` INT;
   ```

 * Remove deprecated code from django-multilingual-ng.
 * Update styles for administation.

#### 0.3.1 ####
 * Refactor tests.
 * Change multilingual data keys in admin to avoid conflicts.

#### 0.3.0 ####
 * Support Django 1.4.
 * Move static files to `static` directory.
 * Fix multilingual model forms (#6).
 * Fix admin forms (#10). Include language into form.
